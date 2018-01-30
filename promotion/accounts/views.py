# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from promotion.accounts.models import (UserProfile, UserGroup,
                                       UserRole)
from promotion.accounts.forms import UserGroupForm

from promotion.accounts.serializers import GroupSerializer


def group_list(request):
    if request.method == 'GET':
        groups = UserGroup.objects.all()
        json_data = GroupSerializer(groups, many=True)
        return JsonResponse(json_data.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serialize = GroupSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize.data, status=201)
        return JsonResponse(serialize.errors, status=400)


def user_list(request):
    return JsonResponse({'success': True, 'users': []})


@csrf_exempt
def user_create(request):
    return JsonResponse({'success': True})


