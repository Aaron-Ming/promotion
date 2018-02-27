# coding: utf-8
'''
记录一些常量
'''

# 用户角色
SUPERT_ADMIN = 'super_admin'
GROUP_ADMIN = 'group_admin'
GROUP_USER = 'group_user'
NORMAL_USER = 'normal_user'
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3
LEVEL_4 = 4
USER_ROLES = [
    {
        'role_name': u'超级管理员',
        'alias_name': SUPERT_ADMIN,
        'role_level': LEVEL_1
    },
    {
        'role_name': u'组管理员',
        'alias_name': GROUP_ADMIN,
        'role_level': LEVEL_2
    },
    {
        'role_name': u'组业务员',
        'alias_name': GROUP_USER,
        'role_level': LEVEL_3
    },
    {
        'role_name': u'会员',
        'alias_name': NORMAL_USER,
        'role_level': LEVEL_4
    },
]
