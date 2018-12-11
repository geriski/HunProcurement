from django.shortcuts import render
from notices.models import RegNumber,Cpv,Nuts
from django_tables2 import RequestConfig
from .tables import RegNumberTable,  RegNumberStatNuts 
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2 import MultiTableMixin
from django.views.generic.base import TemplateView
from django.db.models import Count



from .filters import RegFilter


def index(request):
    
    """The home page for Hungarian Public Procurement Advisory"""
    
    return render(request, 'notices/index.html')

def notices(request):
    table = RegNumberTable(RegNumber.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'notices/notices.html', {'table': table})

class StatRegNumberView(SingleTableMixin, FilterView):
    template_name = 'notices/stats.html'
    #table_pagination = {"per_page": 2}
    #model = RegNumber
    filterset_class = RegFilter
    table_class = RegNumberStatNuts
    
    def get_queryset(self):
        
        qs= RegNumber.objects.values('nuts__text').annotate(darab=Count('nuts__text'))
        qs2=RegNumber.objects.all()   
        return qs

    def get_context_data(self, **kwargs):
        context = super(StatRegNumberView, self).get_context_data(**kwargs)
        
        if  self.filterset.form.is_valid():
            context['table_cmu'] =  RegNumberTable(RegNumber.objects.all())
            context['table_cmu'] = self.filterset.filter_queryset(RegNumber.objects.all())
        
        #context['table_cmu2'] =  self.filterset.RegNumberStatNuts(RegNumber.objects.values('nuts__text').annotate(darab=Count('nuts__text')))
                   
        else:
           context['table_cmu']= RegNumberTable(RegNumber.objects.filter(nuts = '000'))
        return context

class FilteredRegNumberListView(SingleTableMixin, FilterView):
    
    table_class = RegNumberTable
    model = RegNumber
    template_name = 'notices/notices.html'
    
    filterset_class = RegFilter
    
#    def get_context_data(self, **kwargs):
#        """
#        Overridden version of `.TemplateResponseMixin` to inject the table into
#        the template's context.
#        """
#        context = super().get_context_data(**kwargs)
#        context['regnumbers'] = RegNumber.objects.all()
#  
#
#        return context 
       
    
#    def get_table_kwargs(self):
 #       return {
  #      'exclude': ('cpv', )
   #     }

from tablib import Dataset
from .admin import RegNumberResource
def simple_upload(request):
    if request.method == 'POST':
        person_resource = RegNumberResource()
        dataset = Dataset()
        new_regs = request.FILES['myfile']

        imported_data = dataset.load(new_regs.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'notices/simple_upload.html')     
	   
