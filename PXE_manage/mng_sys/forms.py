# -*- coding: utf-8 -*-

from django import forms
from models import *


class UserForm(forms.Form):
    username = forms.CharField(required=True, max_length=30)
    password = forms.CharField(required=True)


class ProgramForm(forms.ModelForm):
    # title = forms.CharField(required=True, max_length=30)
    # author = forms.CharField(required=True,max_length=20)
    # up_file = forms.FileField(required=True,max_length=100)
    # up_time = forms.DateTimeField(required=True)
    class Meta:
        model = Programs
        fields = ['id', 'title', 'slug', 'pid', 'creator', 'des', 'make_time']

#
# class AddUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password', 'fullname', 'group']
#
#
# class User_infoForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'fullname', 'group']
#
#
#
# class ModifyPwdForm(forms.ModelForm):
#     password1 = forms.CharField(required=True, min_length=6)
#     password2 = forms.CharField(required=True, min_length=6)
#
#
# class RoleForm(forms.ModelForm):
#     class Meta:
#         model = Role
#         fields = ['name',
#                   # 'permission'
#                   ]
#
#
# class PermissionForm(forms.ModelForm):
#     class Meta:
#         model = Permission
#         fields = [""]
