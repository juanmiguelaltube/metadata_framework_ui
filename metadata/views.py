from dal import autocomplete
from metadata import models 
from metadata import serializers 
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


def index(request):
    return HttpResponse("This is the index page. Add me to the urls.py router if you want to see me.")

class SchemaFieldAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return models.SchemaField.objects.none()

        qs = models.SchemaField.objects.all()

        if self.q:
            qs = qs.filter(field__icontains=self.q)

        return qs

class MetadataList(APIView):
    """
    List all metadata, or create a new metadata.
    """
    def get(self, request, format=None):
        metadatas = models.Metadata.objects.all()
        serializer = serializers.MetadataDisplaySerializer(metadatas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.MetadataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MetadataDetail(APIView):
    """
    Retrieve, update or delete a metadata instance.
    """
    def get_object(self, pk):
        try:
            return models.Metadata.objects.get(id=pk)
        except models.Metadata.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        metadata = self.get_object(pk=pk)
        serializer = serializers.MetadataDisplaySerializer(metadata)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        metadata = self.get_object(pk=pk)
        serializer = serializers.MetadataSerializer(metadata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk, format=None):
        metadata = self.get_object(pk=pk)
        metadata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class SchemaFieldList(APIView):
    """
    List all schema fields, or create a new schema.
    """
    def get(self, request, format=None):
        schema_fields = models.SchemaField.objects.all()
        serializer = serializers.SchemaFieldSerializer(schema_fields, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.SchemaFieldSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchemaFieldDetail(APIView):
    """
    Retrieve, update or delete a schema instance.
    """
    def get_object(self, pk):
        try:
            return models.SchemaField.objects.get(id=pk)
        except models.SchemaField.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        schema_field = self.get_object(pk=pk)
        serializer = serializers.SchemaFieldSerializer(schema_field)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        schema_field = self.get_object(pk=pk)
        serializer = serializers.SchemaFieldSerializer(schema_field, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk, format=None):
        schema_field = self.get_object(pk=pk)
        schema_field.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
