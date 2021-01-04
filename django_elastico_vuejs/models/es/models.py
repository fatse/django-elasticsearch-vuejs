from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text
from elasticsearch_dsl.connections import connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])


class ArticleDocument(Document):
    title = Text(analyzer='snowball', fields={'raw': Keyword()})
    body = Text(analyzer='snowball')
    tags = Keyword()
    published_from = Date()
    lines = Integer()

    class Index:
        name = 'blog'
        settings = {
            'number_of_shards': 2,
        }

    def save(self, **kwargs):
        self.lines = len(self.body.split())
        return super(ArticleDocument, self).save(**kwargs)

    def is_published(self):
        return datetime.now() >= self.published_from


def init_es():
    # create the mappings in elasticsearch
    ArticleDocument.init()
