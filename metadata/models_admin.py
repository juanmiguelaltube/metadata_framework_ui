from django.contrib import admin
from metadata.models_form import MetadataForm
from metadata.models import Metadata

class MetadataAdmin(admin.ModelAdmin):
    form = MetadataForm
    list_display = ('field','factory')
    list_filter = ('field__data_source__name','field__cbs__name')

class SchemaFieldAdmin(admin.ModelAdmin):
    list_display = ('cbs','data_source','field','whitelist')
    list_filter = ('cbs__name','data_source__name','whitelist')