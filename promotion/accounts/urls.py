from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from promotion.accounts.views import GroupViewSet

group_list = GroupViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = [
    url(r'^group_list/$', group_list, name='group_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
