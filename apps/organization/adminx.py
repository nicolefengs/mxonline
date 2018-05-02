#coding=utf-8
from organization.models import CityDict, CourseOrg, Teacher
import xadmin


class CityDictAdmin(object):
    list_display=['name','desc','add_time']
    search_fields=['name','desc']
    list_filter=['name','desc','add_time']

class CourseOrgAdmin(object):
    list_display=['name','desc','click_nums','fav_nums']
    search_fields=['name','desc','click_nums','fav_nums']
    list_filter=['name','desc','click_nums','fav_nums']

class TeacherAdmin(object):
        list_display = ['org', 'name', 'work_years', 'work_years', 'work_company']
        search_fields = ['org', 'name', 'work_years', 'work_years', 'work_company']
        list_filter = ['org', 'name', 'work_years', 'work_years', 'work_company']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download','add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'add_time','add_time']


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
