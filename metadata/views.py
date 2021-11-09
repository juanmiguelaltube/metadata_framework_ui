from django.http import HttpResponse
from dal import autocomplete
from metadata.models import SchemaField, Metadata
from metadata.serializers import MetadataSerializer
from rest_framework import viewsets
from rest_framework import permissions


def index(request):
    return HttpResponse("This site is dark and full of terrors")

class SchemaFieldAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return SchemaField.objects.none()

        qs = SchemaField.objects.all()

        if self.q:
            qs = qs.filter(field__istartswith=self.q)

        return qs


class MetadataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Metadata to be viewed or edited.
    """
    queryset = Metadata.objects.all().order_by('schema_field')
    serializer_class = MetadataSerializer
    permission_classes = [permissions.IsAuthenticated]