from django.contrib import admin
from .models import Links

# Register your models here.
# 配置admin后台站点的信息，注册模型为Links
# 创建管理员命令：python manage.py createsuperuser
# 管理员名称：niki / niki123456

class LinksAdmin(admin.ModelAdmin):
    list_display = ['id','environment','link','account','password']

admin.site.register(Links,LinksAdmin)