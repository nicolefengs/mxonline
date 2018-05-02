#coding=utf-8
from __future__ import unicode_literals

from django.apps import AppConfig


class OrganizationConfig(AppConfig):
    name = 'organization'
    # 后台收起来显示中文
    verbose_name = u"机构管理"