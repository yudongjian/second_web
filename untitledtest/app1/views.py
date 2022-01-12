from django.shortcuts import render
from app1 import models
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
import random,json
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
def login(request):
    return render(request, 'login.html')


# deal with login
def dologin(request):
    name = request.POST.get('username')
    pwd = request.POST.get('password')
    print('name:', name)
    print('pwd:', pwd)
    try:
        user = models.User.objects.get(username=name)
    except Exception as err:
        print('账号密码错误')
        return redirect(reverse('login'))
    # if user exist.
    # input password comparison with database password
    if user:
        input_pwd = fun_package.get_self_md5(user.password_salt, pwd)
        print('input pwd:', pwd)
        print('ipput salt pwd:', input_pwd)
        print('user.password_hash:', user.password_hash)
        if input_pwd == user.password_hash:
            request.session['adminuser'] = user.nickname
            return redirect(reverse('index'))
    print('账号密码错误')
    return render(request, 'login.html', {'info': '账号或密码错误'})


# main page
# @login_required
def index(request):
    return render(request, 'index2.html')


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


def add_data(request):
    return render(request, 'add_data.html')


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
