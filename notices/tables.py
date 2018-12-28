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
    min_amount = tables.Column('Minimum összeg')
    max_amount = tables.Column('Maximum összeg')
    avg_amount = tables.Column('Átlag összeg')
    
    def render_nuts__text(self, record):
        return str(record['nuts__text'])
    
    def render_darab(self, record):
        return str(record['darab'])
    
    def render_min_amount(self, record):
        return str(record['min_amount'])

    def render_max_amount(self, record):
        return str(record['max_amount'])
    
    def render_avg_amount(self, record):
        return str(record['avg_amount'])
    
class RegNumberStatAmount(tables.Table):

    
    amount = tables.Column('Összeg')
    minimum = tables.Column('Minimum')
    
    def render_amount_min(self, record):
        return str(record['amount'])
    
    def render_minimum(self, record):
        return str(record['minimum'])  

    
    
        
