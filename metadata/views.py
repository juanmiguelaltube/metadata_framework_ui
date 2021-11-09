from dal import autocomplete
from metadata.models import Factory, SchemaField, Metadata
from metadata.serializers import MetadataSerializer
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
            return SchemaField.objects.none()

        qs = SchemaField.objects.all()

        if self.q:
            qs = qs.filter(field__istartswith=self.q)

        return qs

class MetadataList(APIView):
    """
    List all metadata, or create a new metadata.
    """
    def get(self, request, format=None):
        metadatas = Metadata.objects.all()
        serializer = MetadataSerializer(metadatas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MetadataSerializer(data=request.data)
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
            return Metadata.objects.get(id=pk)
        except Metadata.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        metadata = self.get_object(pk=pk)
        serializer = MetadataSerializer(metadata)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        metadata = self.get_object(pk=pk)
        serializer = MetadataSerializer(metadata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk, format=None):
        metadata = self.get_object(pk=pk)
        metadata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        