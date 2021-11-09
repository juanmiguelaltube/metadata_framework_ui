from metadata.models import Metadata,SchemaField
from rest_framework import serializers


class SchemaFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemaField
        fields = ['field','whitelist']

class MetadataSerializer(serializers.ModelSerializer):
    field = SchemaFieldSerializer(many=False)
    factory = serializers.StringRelatedField(many=False)

    class Meta:
        model = Metadata
        fields = ['field','factory','condition','format_in', 'format_out']