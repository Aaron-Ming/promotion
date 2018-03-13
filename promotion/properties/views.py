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
        # import pdb; pdb.set_trace()
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



#select * from properties_assets where instruction->"$.产权"="90大产权"
#select * from properties_assets where instruction = CAST('{"产权":"90大产权"}' as JSON)\G;
#select * from properties_ass ets where instruction = CAST('{"产权":"90大产权"}' as JSON) or spot = CAST('{"配套":"医院"}' as json)\G;
#select * from properties_assets where instruction->>"$.产权" = "90大产权" or spot->>"$.配套"="医院";


# 选择房龄区间  
# 年代选择

# 选择房产面积区间
# 面积从大到小
# 面积从小到大

# 债权从高到低
# 债权从低到高

# 最新发布

# 选择城市

# 房产性质-->住宅、商业
# 装修类型
# select * from properties_assets where parms->>"$.性质" = "住宅" or spot->>"$.配套"="地铁、医院@#！";
# select * from properties_assets where parms = CAST('{"性质":"住宅"}' as JSON) or parms = CAST('{"朝向":"南北"}' as json)\G;
# select * from properties_assets where parms = CAST('{"姓名":"明广振"}' as JSON) or parms = CAST('{"姓名":"明广振"}' as json)\G;
# select * from properties_assets where parms = CAST('{"性质":"住宅", "朝向":"南北"}' as JSON)