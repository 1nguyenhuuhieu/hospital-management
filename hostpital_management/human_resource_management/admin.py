from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

from import_export import resources
# Register your models here.

# Khai báo cho module import-export django
class StaffResource(resources.ModelResource):
    class Meta:
        model = Staff
        fields = ('id', 'user', 'full_name', 'phone', 'detail',)



@admin.register(Staff)
class StaffAdmin(ImportExportModelAdmin):
    resource_class = StaffResource
    search_fields = ['full_name']


