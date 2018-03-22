# -*- coding: utf-8 -*-
from rest_framework import serializers, validators
from promotion.properties.models import Category, Assets, AssetsImg


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'instruction',
                  'parms', 'spot',)

    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)
        for validator in self.fields['category_name'].validators:
            if isinstance(validator, validators.UniqueValidator):
                validator.message = u'资产类型已经存在！'

class PropertySerializer(serializers.ModelSerializer):
    instruction = serializers.JSONField(binary=False)
    parms = serializers.JSONField(binary=False)
    spot = serializers.JSONField(binary=False)
    category_id = serializers.IntegerField()
    author_id = serializers.IntegerField()
    category_name = serializers.CharField(source='category.category_name', required=False)

    class Meta:
        model = Assets
        fields = ('id', 'title', 'debt_type',
                  'instruction', 'parms', 'bond_institution',
                  'obligor', 'guarantee', 'mortgagor',
                  'spot', 'contacts', 'c_phone', 'fax',
                  'p_address', 'transaction', 'statement',
                  'pub_time', 'category_id', 'author_id',
                  'category_name', 'assets_imgs',)

class AssetsImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsImg
        fields = ('id', 'large', 'middle', 'small')
