# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# from rest_framework import mixins
# from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from promotion.accounts.models import (UserProfile, UserGroup,
                                       UserRole)
from promotion.accounts.forms import UserGroupForm
from promotion.accounts.serializers import (GroupSerializer,
                                            ProfileSerializer,
                                            RoleSerializer,
                                            UserSerializer)
from promotion.utils.permissions import IsSuperUser


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        res_data = {}
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if not user.is_staff:
            return Response({'error_msg': u'权限不足，请登入后台管理员账户'},
                             status=status.HTTP_403_FORBIDDEN)
        token, created = Token.objects.get_or_create(user=user)
        res_data.update({
            'token': token.key,
            'is_superuser': user.is_superuser,
            'is_staff': user.is_staff,
            'user_id': user.id,
            'username': user.username,
            'profile_id': '',
            'id_name': '',
            'group_id': '',
            'group_name': '',
            'role_id': '',
            'role_name': '',
            'role_level': '',
        })
        if hasattr(user, 'userprofile'):
            profile = user.userprofile
            res_data.update({
                'profile_id': profile.id,
                'id_name': profile.id_name,
                'group_id': profile.group.id,
                'group_name': profile.group.group.group_name,
                'role_id': profile.role.id,
                'role_name': profile.role.role_name,
                'role_level': profile.role.role_level,
            })
        return Response(res_data)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsSuperUser, )


class RoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = RoleSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        res_data = request.data
        username = res_data.get('mobile', '')
        password = res_data.get('password', '')
        user = User.objects.create_user(username=username, password=password)
        request.data['user'] = user.id
        return super(ProfileViewSet, self).create(request, *args, **kwargs)


def check_mobile(request):
    mobile = request.GET.get('mobile', '')
    if User.objects.filter(username=mobile):
        return JsonResponse({'is_used': True})
    else:
        return JsonResponse({'is_used': False})
