"""PXE_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from mng_sys.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^login/$', login, name="login"),
    url(r'^user_create/$', user_create, name="user_create"),
    url(r'^user_operation/$', user_operation, name="user_operation"),
    url(r'^user_edit/$', user_edit, name="user_edit"),
    url(r'^program_list/(?P<id>\d+)/$', program_list, name="program_list"),
    url(r'^make_program/(?P<id>\d+)/$', make_program, name="make_program"),
    url(r'^upload/$', upload, name="upload"),

]
