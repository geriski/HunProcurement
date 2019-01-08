import django_filters


from .tables import RegNumberTable
from .models import RegNumber

STATUS_CHOICES = (
    (0, 'Nem'),
    (1, 'Igen'),
    )


class RegFilter(django_filters.FilterSet):
    text = django_filters.CharFilter(label='Iktatószám', lookup_expr='icontains')
    cpv__text = django_filters.CharFilter(label='CPV-kód',lookup_expr='icontains')
    env = django_filters.ChoiceFilter(empty_label="környezetvédelem",choices=STATUS_CHOICES)
#    nuts__text = django_filters.CharFilter(exclude = True)
    
    class Meta:
        model = RegNumber
        fields = ['text', 'cpv__text','nuts',]
        
        
        

