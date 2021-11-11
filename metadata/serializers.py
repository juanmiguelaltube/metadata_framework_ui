import metadata.models as models
from rest_framework import serializers


class CBSSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CBS
        fields = '__all__'

class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSource
        fields = '__all__'

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Factory
        fields = '__all__'

class SchemaFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SchemaField
        fields = '__all__'

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Metadata
        fields = '__all__'

class MetadataDisplaySerializer(serializers.ModelSerializer):
    field = SchemaFieldSerializer(many=False, read_only=True)

    class Meta:
        model = models.Metadata
        fields = '__all__'