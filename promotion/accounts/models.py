# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

ROLE_LEVEL = (
    (1, 'super_admin'),
    (2, 'group_admin'),
    (3, 'group_user'),
)

# 用户组
class UserGroup(models.Model):
    group_name = models.CharField(max_length=15, verbose_name=u'组名称')
    alias_name = models.CharField(max_length=15, verbose_name=u'组别名')
    group_admin = models.ForeignKey('UserProfile', related_name='userprofile',
                                    verbose_name=u'组管理员', blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = u'用户组'

    def __unicode__(self):
        return self.alias_name

# 用户角色
class UserRole(models.Model):
    role_name = models.CharField(max_length=15, verbose_name=u'角色名称')
    alias_name = models.CharField(max_length=15, verbose_name=u'角色别名中文')
    role_level = models.IntegerField(default=3, verbose_name=u'角色级别', choices=ROLE_LEVEL)

    class Meta:
        verbose_name = verbose_name_plural = u'用户角色'

    def __unicode__(self):
        return self.alias_name

# 用户信息
class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'用户')
    mobile = models.CharField(max_length=15, verbose_name=u'手机号')
    id_number = models.CharField(max_length=20, verbose_name=u'身份证号')
    credit_code = models.CharField(max_length=64, verbose_name=u'统一社会信用代码',
                                   blank=True, null=True)
    avatar = models.CharField(max_length=256, verbose_name=u'头像',
                              blank=True, null=True)
    id_name = models.CharField(max_length=15, verbose_name=u'身份证用户名')
    occupation = models.CharField(max_length=15, verbose_name=u'职业',
                                  blank=True, null=True)
    role = models.ForeignKey(UserRole, verbose_name=u'角色')
    group = models.ForeignKey('UserGroup', verbose_name=u'用户组', related_name='usergroup')
    active = models.BooleanField(default=False, verbose_name=u'用户是否激活')

    class Meta:
        verbose_name = verbose_name_plural = u'用户信息'

    def __unicode__(self):
        return self.id_name
