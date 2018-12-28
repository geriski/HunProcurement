import django_filters
from .tables import RegNumberTable
from .models import RegNumber
from django_filters.widgets import BooleanWidget


class RegFilter(django_filters.FilterSet):
    text = django_filters.CharFilter(label='Iktatószám', lookup_expr='icontains')
    cpv__text = django_filters.CharFilter(label='CPV-kód',lookup_expr='icontains')
    env = django_filters.BooleanFilter(widget=BooleanWidget())
#    nuts__text = django_filters.CharFilter(exclude = True)
    
    class Meta:
        model = RegNumber
        fields = ['text', 'cpv__text','nuts',]
        
        
        

