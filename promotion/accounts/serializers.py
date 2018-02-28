# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers, validators
from promotion.accounts.models import UserGroup, UserProfile


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('id', 'group_name', 'alias_name', 'group_admin')

    def __init__(self, *args, **kwargs):
        super(GroupSerializer, self).__init__(*args, **kwargs)
        for validator in self.fields['group_name'].validators:
            if isinstance(validator, validators.UniqueValidator):
                validator.message = u'区域组名称已经存在！'
        for validator in self.fields['alias_name'].validators:
            if isinstance(validator, validators.UniqueValidator):
                validator.message = u'区域组别名已经存在！'


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
    class Meta:
        model = UserProfile
        fields = ('mobile', 'id_number', 'credit_code', 'avatar',
                  'id_name', 'occupation', 'role', 'group')

    def create(self, validated_data):
        profile = super(ProfileSerializer, self).create(validated_data)
        return profile
