from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Categoria

@registry.register_document
class CategoryDocument(Document):

    """descuento = fields.ObjectField(properties={
        'titulo':fields.TextField(),
        'porcentaje':fields.FloatField()
    })"""

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
         #related_models = ["Descuento"]