from django.conf.urls import url
from promotion.accounts.views import (user_list, )

urlpatterns = [
    url(r'^user_list/$', user_list, name='accounts_users')
]