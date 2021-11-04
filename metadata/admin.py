from django.contrib import admin

from .models import CBS,DataSource,Factory,Metadata,SchemaField

admin.site.register(CBS)
admin.site.register(DataSource)
admin.site.register(Factory)
admin.site.register(Metadata)
admin.site.register(SchemaField)