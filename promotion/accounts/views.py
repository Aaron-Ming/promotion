# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse

# from rest_framework import mixins
# from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from promotion.accounts.models import (UserProfile, UserGroup,
                                       UserRole)
from promotion.accounts.serializers import (GroupSerializer,
                                            ProfileSerializer,
                                            RoleSerializer)
from promotion.utils.permissions import IsSuperUser
from promotion.utils.pagination import BasePagination


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
            if not profile.active:
                return Response({'error_msg': u'用户未激活，请联系管理员激活！'},
                                status=status.HTTP_403_FORBIDDEN)
            res_data.update({
                'profile_id': profile.id,
                'id_name': profile.id_name,
                'group_id': profile.group.id,
                'group_name': profile.group.group_name,
                'role_id': profile.role.id,
                'role_name': profile.role.role_name,
                'role_level': profile.role.role_level,
            })
        if user.is_superuser:
            res_data['role_level'] = 1
        return Response(res_data)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsSuperUser, )


class RoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = RoleSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return UserRole.objects.filter(role_level__gte=2)
        elif hasattr(user, 'userprofile'):
            role = user.userprofile.role
            return UserRole.objects.filter(role_level__gte=role.role_level)
        return []


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser, )
    pagination_class = BasePagination

    def get_queryset(self):
        user = self.request.user
        search_q = self.request.GET.get('search_q', '')
        res_users = UserProfile.objects.filter(user__is_superuser=False)
        if search_q:
            res_users = res_users.filter(Q(mobile__icontains=search_q) |
                                         Q(id_name__icontains=search_q))
        if hasattr(user, 'userprofile'):
            group = user.userprofile.group
            res_users = res_users.filter(group=group)
        is_active = self.request.GET.get('active', 'true')
        if res_users and is_active == 'false':
            res_users = res_users.filter(active=False)
        return res_users

    def set_profile_parms(self, request, user):
        role = UserRole.objects.get(id=request.data.get('role'))
        role_level = role.role_level
        active = request.data.get('active', 'no_action')
        is_staff = role_level < 4
        if is_staff:
            user.is_staff = is_staff
            user.save()
        request.data['user'] = user.id
        creatd_user = request.user
        if creatd_user.is_superuser and active == 'no_action':
            request.data['active'] = True
        elif hasattr(creatd_user, 'userprofile') and active == 'no_action':
            profile = creatd_user.userprofile
            if profile.role.role_level < 3:  # role_level < 3 为超级管理员／组管理员
                request.data['active'] = True

    def create(self, request, *args, **kwargs):
        res_data = request.data
        username = res_data.get('mobile', '')
        password = res_data.get('password', '')
        user = User.objects.create_user(username=username, password=password)
        self.set_profile_parms(request, user)
        return super(ProfileViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        profile = self.get_object()
        password = request.data.get('password', None)
        if password:
            user = profile.user
            user.set_password(password)
        self.set_profile_parms(request, profile.user)
        return super(ProfileViewSet, self).update(request, *args, **kwargs)


def check_mobile(request):
    mobile = request.GET.get('mobile', '')
    is_add = request.GET.get('is_add', '')
    if not is_add == 'true':
        profile_id = request.GET.get('profile_id', '')
        profile = UserProfile.objects.get(id=profile_id)
        if mobile == profile.mobile:
            return JsonResponse({'is_used': False})
    if User.objects.filter(username=mobile):
        return JsonResponse({'is_used': True})
    else:
        return JsonResponse({'is_used': False})
