# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from models import *
from forms import *
from extra import make_dirs
# import chunk
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
        program_list = Programs.objects.filter(pid=0).order_by("id")
        pid = 0
        return render(request, 'index.html', {
            "program_list": program_list,
            "id": pid
        })


def user_create(request):
    return render(request, "user_create.html")


def user_operation(request):
    return render(request, "user_operation.html")


def user_edit(request):
    return render(request, "edit.html")


def program_list(request, id):

    if request.method == "GET":
        # slug = request.GET.get("slug")
        id = id
        program_list = Programs.objects.filter(pid=id).order_by("id")
        up_files = Files.objects.filter(program_id=id).order_by("id")
        return render(request, "index.html", {
            "id": id,
            "program_list": program_list,
            "up_files": up_files,
        })
# def program_list(request, slug):
#     return render(request, "program_list.html")


def make_program(request, id):
    if request.method == "POST":
        program_form = ProgramForm(request.POST)
        if program_form.is_valid():
            eq_programs = Programs.objects.filter(pid=id).values("title")
            title_list = []
            for i in range(len(eq_programs)):
                title_list.append(eq_programs[i]['title'])
            program_title = request.POST.get("title")
            if program_title in title_list:
                msg = "项目已存在，请重新创建项目"
                return render(request, "make_program.html",{
                    "msg": msg,
                    "id":id
                })
            else:
                pr_slug = Programs.objects.filter(id=id).values("slug")[0]['slug']
                print(pr_slug)
                slug1 = request.POST.get("slug")
                slug = pr_slug+"\\"+slug1
                program_creator = request.POST.get("creator")
                program_des = request.POST.get("des")
                program = Programs()
                program.title = program_title
                program.slug = slug
                program.creator = program_creator
                program.des = program_des
                program.pid = id
                program.save()
            # from PXE_manage.settings import BASE_DIR
            # full_slug =
            # full_slug = os.path.join(os.path.join(BASE_DIR, "media"), "full_slug")
                make_dirs(slug)
                msg = "项目创建成功"
                return render(request, "make_program.html", {
                    "msg": msg,
                    "id": id
                })
        else:
            msg = "格式不正确"
            return render(request, "make_program.html", {
                "msg": msg,
                "id": id
            })
    else:
        # id = id
        return render(request, "make_program.html",{"id": id})


def upload(request, id):
    if request.method == "POST":
        up_form = UploadForm(request.POST, request.FILES)
        if up_form.is_valid():
            file_title = request.POST.get("title")
            eq_files = Files.objects.filter(pid=id).values("title")
            title_list = []
            for i in range(len(eq_files)):
                title_list.append(eq_files[i]['title'])
            if file_title in title_list:
                msg = "文件已存在"
                return render(request, "upload.html", {
                    "msg": msg,
                    "id": id
                })
            else:
                pr_slug = Files.objects.filter(id=id).values("slug")[0]['slug']
                print(pr_slug)
                slug1 = request.POST.get("slug")
                slug = pr_slug + "\\" + slug1
                file_uploader = request.POST.get("uploader")
                file_des = request.POST.get("des")
                file = Files()
                file.title = file_title
                file.slug = slug
                file.uploader = file
                file.des = file_uploader
                file.pid = id
                file.save()
                # from PXE_manage.settings import BASE_DIR
                # full_slug =
                # full_slug = os.path.join(os.path.join(BASE_DIR, "media"), "full_slug")
                make_dirs(slug)
                msg = "文件创建成功"
                return render(request, "upload.html", {
                    "msg": msg,
                    "id": id
                })
        else:
            msg = "格式不正确"
            return render(request, "upload.html", {
                "msg": msg,
                "id": id
            })




        # up_file = request.FILES.get("up_file", None)
        # print(up_file.name)
        # if not up_file:
        #     msg = "无文件上传"
        #     return render(request, "upload.html", {
        #         "id": id,
        #         "msg": msg,
        #     })
        # destination = open(os.path.join("C:\Users\q", up_file.name), 'wb+')
        # for chunk in up_file.chunks():
        #     destination.write(chunk)
        # destination.close()
        # msg = "文件上传成功"
        # return render(request, "upload.html", {
        #     "id": id,
        #     "msg": msg,
        # })
    else:
        return render(request, "upload.html", {
            "id":id,
        })