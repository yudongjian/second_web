from django.shortcuts import render
from app1 import models
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import redirect
import random
from . import mymd5


# login windows
def login(request):
    return render(request, 'login.html')


# register windows
def register(request):
    return render(request, 'register.html')


# deal with register
def doregister(request):

    pwd = request.POST.get('pwd1')
    name = request.POST.get('username')
    salt = random.randint(111111, 999999)
    pwd_salt = mymd5.get_self_md5(salt, pwd)
    try:
        models.User.objects.create(
            username=name,
            nickname='小华',
            password_hash=pwd_salt,
            password_salt=salt,
            status=1
        )
        return render(request, 'login.html', {'info': '插入成功'})
    except Exception as err:
        print(err)
        return render(request, 'register.html', {'info': '插入失败'})


# deal with login
def dologin(request):
    name = request.POST.get('username')
    pwd = request.POST.get('password')
    request.session['adminuser'] = '123456789'
    return redirect(reverse('index'))


# main page
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