from django.contrib import admin
from .models_form import MetadataForm
from .models import Metadata

class MetadataAdmin(admin.ModelAdmin):
    form = MetadataForm
    list_display = ('schema_field','factory', 'params')
    #list_filter = ('schema_field__data_source',)