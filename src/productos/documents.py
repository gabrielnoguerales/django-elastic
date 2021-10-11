from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Categoria, Producto

@registry.register_document
class CategoryDocument(Document):

    class Index:
        name = 'categoria'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Categoria
         fields = [
             'titulo',
         ]

@registry.register_document
class ProductDocument(Document):
    categoria = fields.ObjectField(properties={
        'titulo': fields.TextField()
    })

    class Index:
        name = 'producto'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Producto
         fields = [
             'titulo',
             'descripcion'
         ]

         related_models = ["Categoria"]