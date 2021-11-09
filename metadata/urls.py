from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(
        r'^field-autocomplete/$',
        views.SchemaFieldAutocomplete.as_view(),
        name='field-autocomplete',
    ),
    path('', views.index, name='index'),
]