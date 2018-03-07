# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    '''super permission control'''

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class GroupAdmin(BasePermission):
    '''区域组长权限'''

    def has_permission(self, request, view):
        user = request.user
        if hasattr(user, 'userprofile'):
            profile = user.userprofile
            return profile.role.alias_name == 'group_admin'
