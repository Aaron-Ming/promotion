# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission
from promotion.properties.models import Assets

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

class AssetsDel(BasePermission):
    '''资产删除权限'''
    def has_permission(self, request, view):
        # import pdb; pdb.set_trace()
        if request.method == 'DELETE':
            user = request.user
            assets_id = request.parser_context['kwargs'].get('pk')
            assets = Assets.objects.get(id=assets_id)
            user_id = user.id
            author_id = assets.author_id
            return user_id == author_id
        return True