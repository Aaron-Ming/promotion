# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from promotion.properties.models import (Category, Assets, AssetsImg)
from promotion.properties.serializers import CategorySerializer,PropertySerializer,AssetsImgSerializer
from rest_framework.response import Response
from django.http.response import HttpResponseBase
from django.utils.cache import cc_delim_re, patch_vary_headers
from promotion.utils.handler import Ssql
from promotion.utils.handler import QSHandler
from rest_framework import status
from promotion.utils.handler import AssetsImgHandler as AIH


class CategoryViewSet(viewsets.ModelViewSet):
    # queryset = Category.objects.all()
    queryset = Category.objects.order_by('id')
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        category_id = kwargs.get('pk')
        cateAssets = Assets.objects.filter(category_id=category_id)
        if len(cateAssets) != 0:
            return Response(status=410)
        return super(CategoryViewSet, self).destroy(request, *args, **kwargs)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all()
    serializer_class = PropertySerializer

    def list(self, request, *args, **kwargs):
        # keys = [{'key': 'parms', 'val': (u'性质', u'住宅')},
        #         {'key': 'parms', 'val': (u'面积（平米）', (90, 120))},
        #         {'key': 'instruction', 'val': (u'债权本金（万）', (0, 2000))},
        #         {'key': 'instruction', 'val': (u'债权利息（万）', (2, 3))}]
        keys = [{'key': 'spot', 'val': (u'汽车参数1', u'w123')},]
        # sql = Ssql(keys).sql
        # queryset = Assets.objects.raw(sql)
        # queryset = self.filter_queryset(self.get_queryset())
        requestType = request.GET.get('t')
        user_id = request.user.id
        region_id = request.GET.get('region_id')
        search_keys = request.GET.get('keys', keys)
        qsinstance = QSHandler(requestType, user_id, region_id, search_keys)
        queryset = qsinstance.queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        request_data = request.data
        assets_imgs = request_data.get('assets_imgs', None)
        assets_id = request_data.get('id')
        AIH(assets_id, assets_imgs).execute('update')
        return super(PropertyViewSet, self).update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        assets_id = serializer.data.get('id')
        assets_imgs = request.data.get('assets_imgs')
        AIH(assets_id, assets_imgs).execute('create')
        assets_imgs = Assets.objects.get(id=assets_id).assets_imgs
        serializer_data = serializer.data
        serializer_data['assets_imgs'] = assets_imgs
        return Response(serializer_data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        assets_id = kwargs.get('pk')
        AIH(assets_id).execute('destroy')
        return super(PropertyViewSet, self).destroy(request, *args, **kwargs)


class AssetsImgViewSet(viewsets.ModelViewSet):
    queryset = AssetsImg.objects.all()
    serializer_class = AssetsImgSerializer