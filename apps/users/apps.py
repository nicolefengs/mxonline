#coding=utf-8
from __future__ import unicode_literals

from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    # 后台收起来显示中文
    verbose_name = u"用户信息"