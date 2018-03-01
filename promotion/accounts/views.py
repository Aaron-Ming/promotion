# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# from rest_framework import mixins
# from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from promotion.accounts.models import (UserProfile, UserGroup,
                                       UserRole)
from promotion.accounts.forms import UserGroupForm
from promotion.accounts.serializers import (GroupSerializer,
                                            ProfileSerializer,
                                            RoleSerializer,
                                            UserSerializer)


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class GroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = GroupSerializer


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
