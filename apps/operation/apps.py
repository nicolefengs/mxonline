#coding=utf8
from __future__ import unicode_literals

from django.apps import AppConfig


class OperationConfig(AppConfig):
    name = 'operation'
    #后台收起来显示中文
    verbose_name=u"用户操作"
