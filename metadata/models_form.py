from django import forms 
from metadata.models import Metadata,SchemaField
from django.utils.translation import gettext_lazy as _
from dal import autocomplete


class MetadataForm(forms.ModelForm):
    field = forms.ModelChoiceField(
        queryset=SchemaField.objects.all(),
        widget=autocomplete.ModelSelect2(url='field-autocomplete',
            attrs={'data-placeholder': 'Search...',
                #'data-minimum-input-length': 3,
            },
        )
    )
    
    class Meta:
        model = Metadata
        fields = '__all__'
        # exclude = ['params']
        # widgets = {
        #     'schema_field': autocomplete.ModelSelect2(url='field-autocomplete')
        # }
        help_texts = {
            'params': _('Some useful help text indeed.'),
        }