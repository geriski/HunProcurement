from django.contrib import admin

from notices.models import RegNumber,Cpv,Nuts

admin.site.register(RegNumber)
admin.site.register(Cpv)
admin.site.register(Nuts)
