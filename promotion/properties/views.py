# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from promotion.properties.models import (Category, Assets)
from promotion.properties.serializers import CategorySerializer,PropertySerializer
from rest_framework.response import Response
from django.http.response import HttpResponseBase
from django.utils.cache import cc_delim_re, patch_vary_headers
from promotion.utils.dbselecter import Ssql


class CategoryViewSet(viewsets.ModelViewSet):
    # queryset = Category.objects.all()
    queryset = Category.objects.order_by('id')
    serializer_class = CategorySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all()
    serializer_class = PropertySerializer

    def list(self, request, *args, **kwargs):
        keys = [{'key': 'parms', 'val': (u'性质', u'住宅')},
                {'key': 'parms', 'val': (u'面积（平米）', (90, 120))},
                {'key': 'instruction', 'val': (u'债权本金（万）', (0, 2000))},
                {'key': 'instruction', 'val': (u'债权利息（万）', (2, 3))}]
        sql = Ssql(keys).sql
        queryset = Assets.objects.raw(sql)
        # sql = 'select * from properties_assets where instruction->>"$.产权" = "{}"'
        # getdata = request.GET.copy()
        # if getdata.get('year'):
        #     get_queryset = Assets.objects.raw(sql.format(getdata['year']))
        #     queryset = self.filter_queryset(get_queryset)
        # else:
        #     queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)