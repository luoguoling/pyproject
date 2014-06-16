__author__ = 'Administrator'
#coding=utf-8
#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^add/$','blog.views.add',name='blog_add'),
    url(r'^list/$','blog.views.list',name='blog_list'),
    url(r'^update-(?P<id>\d+)/$','blog.views.update',name='blog_update'),
    url(r'^delete-(?P<id>\d+)/$','blog.views.delete',name='blog_delete'),
    url(r'^submit/$','blog.views.submit',name='blog_submit'),
    url(r'^register/$','blog.views.register',name='blog_register'),

    )