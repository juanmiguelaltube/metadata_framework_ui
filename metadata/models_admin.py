from django.contrib import admin
from .models_form import MetadataForm
from .models import Metadata
from ajax_select import make_ajax_form

class MetadataAdmin(admin.ModelAdmin):
    #form = MetadataForm
    form = make_ajax_form(Metadata,{'schema_field':'fields'})
    list_display = ('schema_field','factory', 'params')
    #list_filter = ('schema_field__data_source',)