# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
import json
# Create your models here.
from django_mysql.models import JSONField, Model

DEBTS_TYPE = (
    (u'企业', u'企业'),
    (u'个人', u'个人'),
)

class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True,
                                     verbose_name=u'资产类型')
    
    class Meta:
        verbose_name = verbose_name_plural = u'资产分类'

    def __unicode__(self):
        return self.name

class Assets(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'分类')
    title = models.CharField(max_length=32, verbose_name=u'资产名称')
    # 债务类型(公司|个人)
    debt_type = models.CharField(max_length=16, verbose_name=u'债务类型', choices=DEBTS_TYPE)
    # 说明
    instruction = JSONField(verbose_name=u'资产说明')
    # 配套信息
    parms = JSONField(verbose_name=u'配套信息')

    bond_institution = models.CharField(max_length=32, verbose_name=u'债权机构')
    obligor = models.CharField(max_length=8, verbose_name=u'债务人')
    guarantee = models.CharField(max_length=8, verbose_name=u'保证人')
    mortgagor = models.CharField(max_length=8, verbose_name=u'抵押人')
    # 资产亮点
    spot = JSONField(verbose_name=u'资产亮点')
    # 受理公示事项
    contacts = models.CharField(max_length=8, verbose_name=u'联系人')
    c_phone = models.CharField(max_length=16, verbose_name=u'联系人电话')
    fax = models.CharField(max_length=16, verbose_name=u'传真')
    p_address = models.CharField(max_length=64, verbose_name=u'通讯地址')
    # 交易对象及声明
    transaction = models.TextField(verbose_name=u'交易对象')
    statement = models.TextField(verbose_name=u'声明')

    pub_time = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')

    class Meta:
        verbose_name = verbose_name_plural = u'资产信息'

    def __unicode__(self):
        return self.title

    @property
    def json_data(self):
        dit_data = model_to_dict(self)
        dit_data['category'] = self.cate_name
        dit_data['imgs'] = self.get_imgs()
        dit_data['spot'] = dit_data['spot']
        dit_data['parms'] = (dit_data['parms'])
        dit_data['instruction'] = dit_data['instruction']
        # print dit_data['instruction']
        return dit_data

    @property
    def cate_name(self):
        return self.category.category_name

    def get_imgs(self, size='large'):
        imgs = self.assetsimg_set.all()
        return [getattr(img, size).url for img in imgs]


class AssetsImg(models.Model):
    assets = models.ForeignKey(Assets, verbose_name=u'资产')
    large = models.ImageField(upload_to='%Y/%m/%d/')
    middle = models.ImageField(upload_to='%Y/%m/%d/')
    small = models.ImageField(upload_to='%Y/%m/%d/')

    class Meta:
        verbose_name = verbose_name_plural = u'资产图片'


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name=u'评论人')
    assets = models.ForeignKey(Assets, verbose_name=u'资产')
    content = models.TextField(verbose_name=u'评论内容')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name=u'评论时间')

    class Meta:
        verbose_name = verbose_name_plural = u'资产评论'

    def __unicode__(self):
        return u'%s...' % self.content[:10]