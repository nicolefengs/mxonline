#coding=utf-8
from __future__ import unicode_literals

from django.apps import AppConfig


class CoursesConfig(AppConfig):
    name = 'courses'
    # 后台收起来显示中文
    verbose_name = u"课程管理"