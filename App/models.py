from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20)

class Links(models.Model):
    objects = models.Manager()
    environment = models.CharField(max_length=50, verbose_name="环境")
    link = models.CharField(max_length=2048, verbose_name="链接")
    account = models.CharField(max_length=500, verbose_name="账号")
    password = models.CharField(max_length=500, verbose_name="密码")


