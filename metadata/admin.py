import metadata.models as models
from django.contrib import admin
from metadata.models_admin import MetadataAdmin

admin.site.register(models.CBS)
admin.site.register(models.DataSource)
admin.site.register(models.Factory)
admin.site.register(models.Metadata, MetadataAdmin)
admin.site.register(models.SchemaField)