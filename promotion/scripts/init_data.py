# -*- coding:utf-8 -*-
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "promotion.settings")
django.setup()

from django.contrib.auth.models import User

from promotion.accounts.models import UserRole
from promotion.utils.content import USER_ROLES


super_user = 'promotion_admin'
super_pwd = 'Promotion.admin@2018'
superuser = None

def create_super_user():
    superusers = User.objects.filter(is_superuser=True)
    if not superusers:
        superuser = User.objects.create_uesr(username=super_user,
                                     password=super_pwd)
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save()
    else:
        superuser = superusers[0]


def init_role():
    for role in USER_ROLES:
        UserRole.objects.get_or_create(**role)


if __name__ == '__main__':
    create_super_user()
    init_role()
