from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from promotion.accounts.views import (GroupViewSet, Login,
                                      ProfileViewSet)

group_list = GroupViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

group_detail = GroupViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

user_list = ProfileViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

user_detail = ProfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    url(r'^login/$', Login.as_view(), name='account_login'),
    url(r'^groups/$', group_list, name='group_list'),
    url(r'^groups/(?P<pk>\d+)/$', group_detail, name='group_detail'),
    url(r'^users/$', user_list, name='user_list'),
    url(r'^users/(?P<pk>\d+)/$', user_detail, name='user_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
