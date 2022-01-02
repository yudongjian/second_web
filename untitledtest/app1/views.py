from django.shortcuts import render
from app1 import models
# Create your views here.


# 主页
def index(request):
    data = models.Food.objects.filter()
    print(data)
    return render(request, 'index.html', {'data': data})