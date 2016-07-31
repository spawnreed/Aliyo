from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<board_id>[0-9]+)/$', views.detail, name='detail'),


]
