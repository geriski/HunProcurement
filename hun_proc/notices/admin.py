from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from notices.models import RegNumber,Cpv,Nuts

#admin.site.register(RegNumber)
admin.site.register(Cpv)
admin.site.register(Nuts)


#https://django-import-export.readthedocs.io/en/latest/getting_started.html#creating-import-export-resource

class RegNumberResource(resources.ModelResource):
    
    #cpv= Field(attribute='text')
    #nuts= Field(attribute='text')
    
    class Meta:
        model = RegNumber
        import_id_fields = ['text']
        fields = ['text','cpv','nuts']
        
@admin.register(RegNumber)        
class RegNumberResourceAdmin(ImportExportModelAdmin):
    resource_class = RegNumberResource