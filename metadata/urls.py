from django.urls import path
from ajax_select import urls as ajax_select_urls
from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^ajax_select/', include(ajax_select_urls)),
    path('', views.index, name='index'),
]