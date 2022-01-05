from django.test import TestCase

# Create your tests here.

print('hello')
import hashlib
import random


def get_md5(str1='123456kjfskj'):
    password = str1
    m = hashlib.md5(password.encode())  # 加密。md5加密是不可逆的
    print(m.hexdigest())  # 加密之后得到的是32位的字符串，打印密文


def get_self_md5(str2, salt):
    # 传入密码和盐
    # 加密的函数
    # 如果传入盐的参数，则加盐
    s = str(str2)  # 类型转换，转成字符串
    if salt:
        s = s + salt
    m = hashlib.md5(s.encode())  # md5加密
    return m.hexdigest()  # 返回密文


a = get_self_md5('123', 'yuyali2010')
print(a)