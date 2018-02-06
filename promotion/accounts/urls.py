from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from promotion.accounts.views import GroupViewSet

group_list = GroupViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

group_detail = GroupViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^groups/$', group_list, name='group_list'),
    url(r'groups/(?P<pk>\d+)/', group_detail, name='group_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
