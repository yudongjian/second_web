from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from app1 import models
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
import random, json
from . import fun_package
import logging
import time
import os


# register windows
def register(request):
    return render(request, 'register.html')


# deal with register
def doregister(request):
    pwd = request.POST.get('pwd1')
    name = request.POST.get('username')
    salt = str(random.randint(111111, 999999))
    md5_pwd = fun_package.get_self_md5(salt, pwd)
    print('pwd:'+ pwd)
    print('register salt:' + salt)
    print('register md5_pwd:' + md5_pwd)
    try:
        models.User.objects.create(
            username=name,
            nickname='小华',
            password_hash=md5_pwd,
            password_salt=salt,
            status=1
        )
        # return render(request, 'login.html', {'info': '插入成功'})
        return redirect(reverse('login'))

    except Exception as err:
        # return render(request, 'register.html', {'info': '插入失败'}
        return redirect(reverse('register'))


# login windows
def login1(request):
    return render(request, 'login.html')


# login windows vue
def login2(request):
    return render(request, 'login-vue.html')


def logout_view(request):
    logout(request)
    return render(request, 'login.html')


def dologin(request):
    print('dologin 被调用了...')
    print(request.POST)
    name = request.POST.get('username')
    pwd = request.POST.get('password')
    print('name:', name)
    print('pwd:', pwd)
    user = authenticate(request, username=name, password=pwd)

    if user is not None:
        login(request, user)
        return redirect(reverse('index'))

    else:
        print('账号密码错误')
        return redirect(reverse('login'))


# main page
@login_required
def index(request):
    print('这句话执行吗？？？')
    print(request.user)
    return render(request, 'index2.html')


@login_required
def show(request, page_index=1):
    data = models.User.objects.filter()
    data = Paginator(data, 5)
    page_values = data.page_range

    # 处理页码
    if page_index < 1:
        page_index = 1
    if page_index > data.num_pages:
        page_index = data.num_pages

    data = data.page(page_index)
    print(data)
    return render(request, 'show_main.html', {'data': data, 'page_values': page_values, 'page_index': page_index})


@login_required
def add_data(request):
    return render(request, 'add_data.html')


@login_required
def upload_file(request):
    # file = request.FILES.get('file1')
    # print('文件大小为：', file.size)
    # print('文件名：', file.name)
    # if file.size > 1024*1024*1204:
    #     return render(request, 'add_data.html', {'msg': "文件太大"})
    # file_path = os.path.join('static', 'file', file.name)
    # with open(file_path, 'wb') as f:
    #     f.write(file.read())
    #
    # # return render(request, 'add_data.html', {'msg': "上传成功"})
    print('ajax上传了.....')
    return HttpResponse(json.dumps({'flag': 'success'}))


def demo(request):
    return render(request, 'demo.html')