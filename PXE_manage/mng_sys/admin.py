# -*- coding: utf-8 -*-

# from django.contrib import admin
import xadmin
from .models import *
# Register your models here.


class ProgramAdmin(object):
    list_display = ('id', 'title', 'slug', 'pid', 'creator', 'des', 'make_time')


xadmin.site.register(Programs, ProgramAdmin)
