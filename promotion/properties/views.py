# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# from rest_framework import mixins
# from rest_framework import generics
from rest_framework import viewsets

from promotion.properties.models import (Category)
from promotion.properties.forms import CategoryForm
from promotion.properties.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    # queryset = Category.objects.all()
    queryset = Category.objects.order_by('id')
    serializer_class = CategorySerializer
