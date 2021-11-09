from django.contrib import admin
from metadata.models_form import MetadataForm
from metadata.models import Metadata

class MetadataAdmin(admin.ModelAdmin):
    form = MetadataForm
    list_display = ('field','factory')
    #list_filter = ('schema_field__data_source',)