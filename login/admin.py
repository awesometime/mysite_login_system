from django.contrib import admin

# Register your models here.
from . import models
# model注册到后台
admin.site.register(models.User)
admin.site.register(models.ConfirmString)


# 本项目后台admin 账号root1 密码123456