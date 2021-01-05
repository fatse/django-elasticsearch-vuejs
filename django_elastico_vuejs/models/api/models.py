from datetime import datetime
from typing import Optional

from rest_framework import serializers


class Article:
    def __init__(self, title: str, body: str, tags: list, published_from: datetime, is_published: bool, lines: int):
        self.title = title
        self.body = body
        self.tags = tags
        self.published_from = published_from
        self.lines = lines
        self.is_published = is_published


class ArticleRequest:
    def __init__(self, title: str, body: str, tags: list):
        self.title = title
        self.body = body
        self.tags = tags
        self.published_from = datetime.now()


class SearchArticleRequest:
    def __init__(self, title: Optional[str], body: Optional[str], tags: Optional[list] = None,
                 search_input: Optional[str] = None):
        self.title = title
        self.body = body
        self.tags = tags
        self.search_input = search_input


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.ListField()
    published_from = serializers.DateTimeField()
    lines = serializers.IntegerField()
    is_published = serializers.BooleanField()


class ArticleRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.ListField()

    def create(self, validated_data):
        return ArticleRequest(validated_data['title'], validated_data['body'], validated_data['tags'])


class SearchArticleRequestSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    body = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    tags = serializers.ListField(required=False, allow_null=True, allow_empty=True)
    search_input = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return SearchArticleRequest(validated_data.get('title'),
                                    validated_data.get('body'),
                                    validated_data.get('tags'),
                                    validated_data.get('search_input'))
