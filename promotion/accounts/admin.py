# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from promotion.accounts.models import UserGroup, UserRole, UserProfile

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile', 'id_name', 'role', 'group', 'active')
    search_fields = ('user', 'mobile', 'id_name', 'role', 'group', 'active')

class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'alias_name', 'group_admin')
    search_fields = ('group_name', 'alias_name', 'group_admin')

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'alias_name', 'role_level')
    search_fields = ('role_name', 'alias_name', 'role_level')


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)




admin.site.register(UserGroup, UserGroupAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)