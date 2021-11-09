from django.forms import ModelForm, Textarea, RadioSelect
from .models import Metadata
from django.utils.translation import gettext_lazy as _


class MetadataForm(ModelForm):
    class Meta:
        model = Metadata
        fields = '__all__'
        # exclude = ['params']
        # widgets = {
        #     'schema_field': RadioSelect(),
        # }

        help_texts = {
            'params': _('Some useful help text.'),
        }
    