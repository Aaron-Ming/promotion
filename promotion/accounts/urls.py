from django.conf.urls import url
from promotion.accounts.views import (user_list, group_list)

urlpatterns = [
    url(r'^user_list/$', user_list),
    url(r'^group_list/$', group_list)
]