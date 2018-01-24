
from django.conf.urls import url
from promotion.dashboard.views import dashboard

urlpatterns = [
    url(r'^$', dashboard, name='dashboard')
]
