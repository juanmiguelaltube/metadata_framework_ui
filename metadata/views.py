from django.http import HttpResponse
from dal import autocomplete
from metadata.models import SchemaField


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class SchemaFieldAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return SchemaField.objects.none()

        qs = SchemaField.objects.all()

        if self.q:
            qs = qs.filter(field__istartswith=self.q)

        return qs