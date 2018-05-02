#coding=utf-8
from django.conf.urls import url
from courses.views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentView

urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    url(r'^detail/(?P<course_id>.*)/$', CourseDetailView.as_view(), name="course_detail"),

    url(r'^info/(?P<course_id>.*)/$', CourseInfoView.as_view(), name="course_info"),

    url(r'^comment/(?P<course_id>.*)/$', CommentsView.as_view(), name="course_comments"),

    url(r'^add_comment/(?P<course_id>.*)/$', AddCommentView.as_view(), name="add_comment"),

]