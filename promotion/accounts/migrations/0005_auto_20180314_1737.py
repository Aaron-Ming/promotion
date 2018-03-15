# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 17:37
from __future__ import unicode_literals

from django.db import migrations, models
import promotion.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180130_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='id_back',
            field=models.ImageField(blank=True, null=True, upload_to=promotion.accounts.models.profile_img_path, verbose_name='\u8eab\u4efd\u8bc1\u80cc\u9762'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='id_face',
            field=models.ImageField(blank=True, null=True, upload_to=promotion.accounts.models.profile_img_path, verbose_name='\u8eab\u4efd\u8bc1\u6b63\u9762'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='license',
            field=models.ImageField(blank=True, null=True, upload_to=promotion.accounts.models.profile_img_path, verbose_name='\u8425\u4e1a\u6267\u7167'),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='role_level',
            field=models.IntegerField(choices=[(1, 'super_admin'), (2, 'group_admin'), (3, 'group_user'), (4, 'normal_user')], default=4, verbose_name='\u89d2\u8272\u7ea7\u522b'),
        ),
    ]