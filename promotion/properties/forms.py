# -*- coding: utf-8-*-

from django import forms
from promotion.properties.models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ()

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        if not category_name:
            self._errors['category_name'] = self.error_class([u'请输入资产类别名称'])
        if len(category_name) > 15:
            self._errors['category_name'] = self.error_class([u'资产类别名称应少于15个字符'])
        return category_name
