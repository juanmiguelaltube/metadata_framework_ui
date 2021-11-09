from django.urls import path
from metadata import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'metadata', views.MetadataViewSet)

urlpatterns = [
    url(
        r'^field-autocomplete/$',
        views.SchemaFieldAutocomplete.as_view(),
        name='field-autocomplete',
    ),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.index, name='index'),
]