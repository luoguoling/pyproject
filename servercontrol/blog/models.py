#coding=utf-8
from django.db import models
from django.contrib import admin
class Blog(models.Model):
    title = models.CharField(u'标题',max_length=60)
    content = models.TextField(u'正文')
    created_at = models.DateTimeField(u'建立时间',auto_now_add=True)
    updated_at = models.DateTimeField(u'修改时间',auto_now=True)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-updated_at','-created_at']



# Create your models here.
