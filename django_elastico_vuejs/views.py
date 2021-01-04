from django.views.generic import TemplateView
from django_elastico_vuejs.models.api.models import ArticleRequestSerializer, SearchArticleRequestSerializer, \
    Article
from django_elastico_vuejs.models.api.models import ArticleSerializer
from django_elastico_vuejs.models.es.models import init_es, ArticleDocument
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

init_es()

client = Elasticsearch()


class AddStory(APIView):
    def post(self, request):
        serializer = ArticleRequestSerializer(data=request.data)
        serializer.is_valid()
        article_request = serializer.create(serializer.validated_data)

        article_document = ArticleDocument(title=article_request.title,
                                           body=article_request.body,
                                           tags=article_request.tags,
                                           published_from=article_request.published_from)

        article_document.save()
        return Response(data="success", status=status.HTTP_200_OK)


class SearchStory(APIView):
    def post(self, request):
        serializer = SearchArticleRequestSerializer(data=request.data)
        serializer.is_valid()
        search_request = serializer.create(serializer.validated_data)

        if not search_request.title and not search_request.body and not search_request.tags:
            query = Q('match_all')

        else:
            query = Q('match_none')
            if search_request.title:
                query = Q("fuzzy", title=search_request.title)
            if search_request.body:
                query |= Q("fuzzy", body=search_request.body)
            if search_request.tags:
                query |= Q("terms", tags=search_request.tags)

        return execute_search(query)


class SearchStoryV2(APIView):
    def post(self, request):
        serializer = SearchArticleRequestSerializer(data=request.data)
        serializer.is_valid()
        search_request = serializer.create(serializer.validated_data)

        if not search_request.search_input:
            query = Q('match_all')

        else:
            query = Q('match_none')
            query |= Q("fuzzy", title=search_request.search_input)
            query |= Q("fuzzy", body=search_request.search_input)
            query |= Q("terms", tags=[search_request.search_input])

        return execute_search(query)


class Articles(TemplateView):
    template_name = 'django_elastico_vuejs/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def execute_search(query):
    search = ArticleDocument.search().query(query)

    all_results = []

    while True:
        search_results = search.execute().hits
        results = list(
            map(lambda x: Article(x.title, x.body, x.tags, x.published_from, x.is_published, x.lines), search_results))
        if not results:
            break
        all_results += results
        search = search[len(all_results):(len(all_results) + 10)]

    serializer = ArticleSerializer(data=all_results, many=True)
    serializer.is_valid()
    return Response(data=serializer.data, status=status.HTTP_200_OK)
