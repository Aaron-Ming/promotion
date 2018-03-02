# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# from rest_framework import mixins
# from rest_framework import generics
from rest_framework import viewsets

from promotion.properties.models import (Category, Assets)
from promotion.properties.forms import CategoryForm
from promotion.properties.serializers import CategorySerializer,PropertySerializer
from rest_framework.response import Response
from django.http.response import HttpResponseBase
from django.utils.cache import cc_delim_re, patch_vary_headers

class CategoryViewSet(viewsets.ModelViewSet):
    # queryset = Category.objects.all()
    queryset = Category.objects.order_by('id')
    serializer_class = CategorySerializer

# @csrf_exempt
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all()
    # queryset = Assets.objects.raw('select * from properties_assets')
    serializer_class = PropertySerializer

    def list(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        sql = 'select * from properties_assets where instruction->>"$.产权" = "{}"'
        getdata = request.GET.copy()
        if getdata.get('year'):
            get_queryset = Assets.objects.raw(sql.format(getdata['year']))
            queryset = self.filter_queryset(get_queryset)
        else:
            queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



#select * from properties_assets where instruction->"$.产权"="90大产权"
#select * from properties_assets where instruction = CAST('{"产权":"90大产权"}' as JSON)\G;
#select * from properties_assets where instruction = CAST('{"产权":"90大产权"}' as JSON) or spot = CAST('{"配套":"医院"}' as json)\G;

#select * from properties_assets where instruction->>"$.产权" = "90大产权" or spot->>"$.配套"="医院";