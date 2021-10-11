from elasticsearch_dsl.query import Q, MultiMatch, SF, Range
from .documents import ProductDocument

def get_search_products_query(phrase):
    query = Q(
        'multi_match',
        fields=['titulo','descripcion'],
        query=phrase
    )
    return ProductDocument.search().query(query)

def search_products(phrase):
    return get_search_products_query(phrase).to_queryset()