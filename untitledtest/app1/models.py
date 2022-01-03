from django.db import models
from datetime import datetime
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)    # 员工账号
    nickname = models.CharField(max_length=50)    # 昵称
    password_hash = models.CharField(max_length=100)  # 密码
    password_salt = models.CharField(max_length=50)    # 密码干扰值
    status = models.IntegerField(default=1)    # 状态:1正常/2禁用/6管理员/9删除
    create_at = models.DateTimeField(default=datetime.now)    # 创建时间
    update_at = models.DateTimeField(default=datetime.now)    # 修改时间


class Food(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=32)
    category = models.CharField(default='主菜', max_length=16)
    price = models.IntegerField()
    photo_path = models.CharField(max_length=32)
    desc = models.CharField(max_length=32)