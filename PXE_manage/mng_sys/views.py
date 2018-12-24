# -*- coding: utf-8 -*-
from datetime import datetime
import os
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from models import *
from forms import *
# Create your views here.


def login(request):
    """用户登录"""
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            user_name = request.POST.get("username")
            pass_word = request.POST.get("password")
            # user = Users.objects.filter(username=user_name, password=pass_word)
            user = authenticate(username=user_name, password=pass_word)
            # if user.exists():
            if user is not None:
                return HttpResponseRedirect("/")
            else:
                return render(request, "login.html")
        else:
            return render(request, "login.html")
    else:
        return render(request, 'login.html')


def index(request):
    if request.method == "GET":
        program_list = Programs.objects.filter(pid=None).order_by("id")
        return render(request, 'index.html', {"program_list": program_list})


def user_create(request):
    return render(request, "user_create.html")


def user_operation(request):
    return render(request, "user_operation.html")


def user_edit(request):
    return render(request, "edit.html")


def program_list(request, id):

    if request.method == "GET":
        print(id)
        # slug = request.GET.get("slug")
        id = Programs.objects.filter(id=id)
        program_list = Programs.objects.filter(pid=id).order_by("id")
        up_files = Files.objects.filter(program_id=id).order_by("id")
        return render(request, "index.html", {
            "program_list": program_list,
            "up_files": up_files,
        })
# def program_list(request, slug):
#     return render(request, "program_list.html")


def make_program(request, id):
    if request.method == "POST":
        program_form = ProgramForm(request.POST)
        if program_form.is_valid():
            program_title = request.POST.get("title")
            parent_slug = Programs.objects.filter(id=id).values("slug")
            program_slug = os.path.join(parent_slug, program_title)
            program_creator = request.POST.get("creator")
            program_des = request.POST.get("des")
            program_pid = id
            program = Programs()
            program.title = program_title
            program.slug = program_slug
            program.creator = program_creator
            program.des = program_des
            program.pid = program_pid
            program.make_time = datetime.now().date()
            program.save()
            msg = "项目添加成功"
            # from PXE_manage.settings import BASE_DIR
            # full_slug =
            # full_slug = os.path.join(os.path.join(BASE_DIR, "media"), "full_slug")
            os.makedirs(program_title)
            return render(request, "make_program.html", {"msg": msg})
    else:
        return render(request, "make_program.html",)

def upload(request):
    return render(request, "upload.html")
