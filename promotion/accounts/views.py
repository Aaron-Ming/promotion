# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

from promotion.accounts.models import (UserProfile, UserGroup,
									   UserRole)


def group_list(request):
	return JsonResponse({'success': True, 'groups': []})


def user_list(request):
	return JsonResponse({'success': True, 'users': []})


def user_create(request):
	return JsonResponse({'success': True})


def group_create(request):
	return JsonResponse({'success': True})
