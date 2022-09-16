from base64 import encode
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(ImportExportModelAdmin):
    
    pass