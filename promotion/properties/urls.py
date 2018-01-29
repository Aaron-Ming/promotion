#encode: utf-8

from django.conf.urls import url
from promotion.properties import views

urlpatterns = [
    url(r'^assets_list/$', views.assets_query, name='assets_query'),
    url(r'^detail/(?P<assets_id>\d+)', views.assets_detail, name='assets_detail'),
    url(r'^create$', views.assets_create, name='assets_create'),
    url(r'^post$', views.post, name='post'),
]