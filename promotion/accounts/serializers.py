# -*- coding: utf-8 -*-
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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('mobile', 'id_number', 'credit_code', 'avatar',
                  'id_name', 'occupation', 'role', 'group', 'active')
