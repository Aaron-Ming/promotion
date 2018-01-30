# -*- coding: utf-8 -*-
from rest_framework import serializers
from promotion.accounts.models import UserGroup


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('group_name', 'alias_name', 'group_admin')