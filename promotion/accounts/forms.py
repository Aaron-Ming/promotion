# -*- coding: utf-8-*-

from django import forms
from promotion.accounts.models import UserGroup


class UserGroupForm(forms.ModelForm):

    class Meta:
        model = UserGroup
        exclude = ()

    def clean_group_name(self):
        group_name = self.cleaned_data.get('group_name')
        if not group_name:
            self._errors['group_name'] = self.error_class([u'请输入区域名称'])
        if len(group_name) > 15:
            self._errors['group_name'] = self.error_class([u'区域名称应少于15个字'])
        return group_name

    def clean_alias_name(self):
        alias_name = self.cleaned_data.get('alias_name')
        if not alias_name:
            self._errors['alias_name'] = self.error_class([u'请输入区域别名'])
        if len(alias_name) > 15:
            self._errors['alias_name'] = self.error_class([u'区域别名应少于15个字母'])
        return alias_name
