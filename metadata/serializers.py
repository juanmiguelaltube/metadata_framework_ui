from metadata.models import Metadata
from rest_framework import serializers


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = ['schema_field','factory','params']