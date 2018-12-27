import django_filters
from .tables import RegNumberTable
from .models import RegNumber


class RegFilter(django_filters.FilterSet):
    text = django_filters.CharFilter(label='Iktatószám', lookup_expr='icontains')
    cpv__text = django_filters.CharFilter(label='CPV-kód',lookup_expr='icontains')
#    nuts__text = django_filters.CharFilter(exclude = True)
    
    class Meta:
        model = RegNumber
        fields = ['text', 'cpv__text','nuts']
        
        
        

