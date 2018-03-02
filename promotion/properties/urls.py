#encode: utf-8
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from promotion.properties.views import CategoryViewSet, PropertyViewSet

category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

properties_list = PropertyViewSet.as_view({
	'get': 'list',
	'post': 'create',
})

properties_detail = PropertyViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'delete': 'destroy'
})

urlpatterns = [
    url(r'^categorys/$', category_list, name='category_list'),
    url(r'^categorys/(?P<pk>\d+)/', category_detail, name='category_detail'),
    url(r'^properties/$', properties_list, name='properties_list'),
    url(r'^properties/(?P<pk>\d+)/', properties_detail, name='properties_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
