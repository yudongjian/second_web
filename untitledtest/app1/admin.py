from django.contrib import admin
from .models import User
# Register your models here.


class user_manager(admin.ModelAdmin):
    list_display = ['id', 'username', 'nickname', 'status']
    list_display_links = ['username']

    list_filter = ['status']


admin.site.register(User, user_manager)