#coding=utf-8
from datetime import datetime
from .models import EmailVerifyRecord,Banner
from users import models
import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True



class GlobalSettings(object):
    site_title="boo管理系统"
    site_footer="boo在线网"
    # app收起来
    menu_style = "accordion"

class EmailVerifyRecordAdmin(object):
    list_display=['code','code','send_time','send_type']
    search_fields=['code','code','send_type']
    list_filter=['code','code','send_time','send_type']


class BannerAdmin(object):
    list_display=['title','title','url','index','add_time']
    search_fields=['title','title','url','index']
    list_filter=['title','title','url','index','add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
#导航主题设置页面风格
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)