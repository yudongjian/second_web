from django.shortcuts import render
from app1 import models
# Create your views here.


# 主页
def index(request):
    return render(request, 'index2.html')


def show(request):
    return render(request, 'show_main.html')