# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.


class Users(AbstractUser):
    User_Group = (
        (1, '研发一组'),
        (2, '研发二组'),
        (3, '研发三组'),
    )
    id = models.AutoField(primary_key=True, unique=True, verbose_name='工号')
    fullname = models.CharField(max_length=10, verbose_name='姓名')
    group = models.IntegerField(default=1, choices=User_Group, verbose_name='研发组')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.fullname


# class Role(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20, verbose_name='角色')
#     # permissions = models.ManyToManyField('Permission', verbose_name='权限')
#
#     def __unicode__(self):
#         return self.name
#
#
# class Operate(models.Model):
#
#     id = models.AutoField(primary_key=True)
#     operate_id = models.IntegerField(default=0)
#     operate_title = models.CharField(max_length=32, unique=True, verbose_name='权限')
#     # url = models.CharField(max_length=128, unique=True)
#     # program = models.ForeignKey('Program', null=True, blank=True)
#
#     def __unicode__(self):
#         return self.id
#
#
def get_file_path(instance, filename):
    return os.path.join('upload_files', str(instance.id), filename)


class Programs(models.Model):

    # id = models.IntegerField(primary_key=True, unique=True)
    id = models.AutoField(primary_key=True, )
    title = models.CharField(max_length=30, null=True)
    slug = models.SlugField(max_length=80, null=True, blank=True)
    pid = models.IntegerField(null=True, blank=True)
    # pid = models.ForeignKey('self', null=True, blank=True)
    creator = models.CharField(max_length=30, null=True, blank=True)
    des = models.CharField(max_length=80, null=True, blank=True)
    make_time = models.DateTimeField(default=datetime.now, verbose_name='上传时间')

    class Meta:
        verbose_name = "项目名称"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Files(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=True, unique=True)
    slug = models.CharField(max_length=80, null=True, blank=True)
    program_id = models.ForeignKey(Programs, null=False, blank=True)
    uploader = models.CharField(max_length=30, null=True, blank=True)
    des = models.CharField(max_length=80, null=True, blank=True)
    up_time = models.DateTimeField(default=datetime.now, verbose_name='上传时间')

    class Meta:
        verbose_name = "文件名称"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

# class Permission(models.Model):
#     id = models.AutoField(primary_key=True)
#     role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
#     # program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
#     # operate_sum = models.IntegerField(default=0)
#
#     def __unicode__(self):
#         return self.id
#
# class User_Role(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     Role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
