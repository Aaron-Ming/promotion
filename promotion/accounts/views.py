# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from promotion.accounts.models import (UserProfile, UserGroup,
                                       UserRole)
from promotion.accounts.forms import UserGroupForm


def group_list(request):
    return JsonResponse({'success': True, 'groups': []})


def user_list(request):
    return JsonResponse({'success': True, 'users': []})


@csrf_exempt
def user_create(request):
    return JsonResponse({'success': True})


def group_create(request):
    if request.method == 'POST':
        group_form = UserGroupForm(request.POST)
        if group_form.is_valid():
            new_group = group_form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'errors': group_form.errors,
                                 'success': False})
    return JsonResponse({'success': False})
