import django_filters
from django_filters import DateFilter
from .models import *

class PedidoFiltro(django_filters.FilterSet):
    start_date = DateFilter(field_name='data_criacao', lookup_expr='gte')
    end_date = DateFilter(field_name='data_criacao', lookup_expr='lte')

    class Meta:
        model = Pedido
        fields = '__all__'
        exclude = ['cliente', 'data_criacao']
