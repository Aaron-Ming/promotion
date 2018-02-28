# -*- coding: utf-8 -*-
from rest_framework import serializers, validators
from promotion.properties.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name')

    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)
        for validator in self.fields['category_name'].validators:
            if isinstance(validator, validators.UniqueValidator):
                validator.message = u'资产类型已经存在！'