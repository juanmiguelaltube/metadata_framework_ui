from django.urls import path
from metadata import views
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register(r'metadata', views.MetadataViewSet)

urlpatterns = [
    url(
        r'^field-autocomplete/$',
        views.SchemaFieldAutocomplete.as_view(),
        name='field-autocomplete',
    ),
    path('api/metadata/', views.MetadataList.as_view()),
    path('api/metadata/<int:pk>/', views.MetadataDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)