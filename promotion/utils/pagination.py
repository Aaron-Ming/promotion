# -*- coding: utf-8 -*-
'''
    分页样式，根据api自身需要设定分页样式
'''

from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class BasePagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page = 1000
