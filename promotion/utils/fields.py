# -*- coding: utf-8 -*-
'''
    放置一些自定义的 field 类型
'''
import base64

from django.core.files.base import ContentFile
from rest_framework import serializers


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, basestring) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension
            filename = '{0}.{1}'.format(self.field_name, ext)
            data = ContentFile(base64.b64decode(imgstr), name=filename)

        return super(Base64ImageField, self).to_internal_value(data)
