from django.shortcuts import redirect
from django.urls import reverse
import re


class login_middleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("ShopMiddleware")

    def __call__(self, request):

        # 获取当前请求路径
        path = request.path
        print(path)
        url_list = ['/login/', '/dologin/', '/logout/']
        if path not in url_list:
            if "adminuser" not in request.session:
                return redirect(reverse('login'))

        # 请求继续执行下去
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response