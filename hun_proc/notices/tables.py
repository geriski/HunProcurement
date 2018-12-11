import django_tables2 as tables
from .models import RegNumber

class RegNumberTable(tables.Table):
   
    class Meta:
        model = RegNumber
        template_name = 'django_tables2/bootstrap.html'
        qs  = RegNumber.objects.all()
   
class RegNumberStatNuts(tables.Table):

    
    nuts__text = tables.Column('Nuts-kód')
    darab = tables.Column('Gyakoriság')
    
    def render_nuts__text(self, record):
        return str(record['nuts__text'])
    
    def render_darab(self, record):
        return str(record['darab'])
    
   

    
    
        
