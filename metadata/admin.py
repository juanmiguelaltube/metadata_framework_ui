from django.contrib import admin

from metadata.models import CBS,DataSource,Factory,Metadata,SchemaField
from metadata.models_admin import MetadataAdmin

admin.site.register(CBS)
admin.site.register(DataSource)
admin.site.register(Factory)
admin.site.register(Metadata, MetadataAdmin)
admin.site.register(SchemaField)