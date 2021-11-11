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


class SchemaFieldFormattedSerializer(serializers.ModelSerializer):
    cbs = serializers.SlugRelatedField(many=False,read_only=True,slug_field='code')
    data_source = serializers.SlugRelatedField(many=False,read_only=True,slug_field='code')
    class Meta:
        model = models.SchemaField
        fields = '__all__'

class MetadataFormattedSerializer(serializers.ModelSerializer):
    field = SchemaFieldFormattedSerializer(many=False, read_only=True)
    factory = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Metadata
        fields = '__all__'