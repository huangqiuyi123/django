from django.test import TestCase

# Create your tests here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse

from App.models import User


# 数据库操作，添加数据
def testdb(request):
    test1 = User(name='niki')
    test1.save()
    return HttpResponse("添加数据成功")


def querry(request):
    response = ''
    response1 = ''

    list = User.objects.all()
    res = User.objects.filter(id=1)
    # User.objects.order_by('name') [0:1]
    User.objects.order_by("name")[0:1]

    User.objects.order_by('id')
    # User.objects.filter(name = "name").order_by(id)

    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse(response)
