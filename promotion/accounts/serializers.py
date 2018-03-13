# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers, validators
from promotion.accounts.models import UserGroup, UserProfile, UserRole


class GroupSerializer(serializers.ModelSerializer):
    group_admin_name = serializers.CharField(source='group_admin.id_name', required=False)

    class Meta:
        model = UserGroup
        fields = ('id', 'group_name', 'alias_name', 'group_admin',
                  'group_admin_name')

    def __init__(self, *args, **kwargs):
        super(GroupSerializer, self).__init__(*args, **kwargs)
        for validator in self.fields['group_name'].validators:
            if isinstance(validator, validators.UniqueValidator):
                validator.message = u'区域组名称已经存在！'
        for validator in self.fields['alias_name'].validators:
            if isinstance(validator, validators.UniqueValidator):
                validator.message = u'区域组别名已经存在！'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ('id', 'role_name', 'role_level')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return User


class ProfileSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.role_name', required=False)
    group_name = serializers.CharField(source='group.group_name', required=False)
    role_level = serializers.IntegerField(source='role.role_level', required=False)

    class Meta:
        model = UserProfile
        fields = ('id', 'mobile', 'id_number', 'credit_code', 'avatar',
                  'id_name', 'occupation', 'role_name', 'group_name',
                  'role', 'group', 'user', 'active', 'role_level')
