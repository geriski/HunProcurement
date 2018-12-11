from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from notices.models import RegNumber,Cpv,Nuts

#admin.site.register(RegNumber)
#admin.site.register(Cpv)
#admin.site.register(Nuts)


#https://django-import-export.readthedocs.io/en/latest/getting_started.html#creating-import-export-resource

class RegNumberResource(resources.ModelResource):
    
    #cpv= Field(attribute='text')
    #nuts= Field(attribute='text')
    
    class Meta:
        model = RegNumber
        import_id_fields = ['text']
#        fields = ['text','cpv','nuts']
        widgets = {
                'date': {'format': '%Y.%m.%d.'},
                }

class CpvResource(resources.ModelResource):
   
    class Meta:
        model = Cpv
        import_id_fields = ['id']

        
class NutsResource(resources.ModelResource):
   
    class Meta:
        model = Nuts
        import_id_fields = ['id']

        
       
@admin.register(RegNumber)        
class RegNumberResourceAdmin(ImportExportModelAdmin):
    resource_class = RegNumberResource
  
@admin.register(Cpv)        
class CpvResourceAdmin(ImportExportModelAdmin):
    resource_class = CpvResource
   
@admin.register(Nuts)        
class NutsResourceAdmin(ImportExportModelAdmin):
    resource_class = NutsResource