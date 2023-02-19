import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

'''例1：django.http.HttpResponse() 来输出 "Hello World！"。该方式将数据与视图混合在一起，不符合 Django 的 MVC 思想'''


def hello(request):
    response = HttpResponse()
    response.content = "Hello world!"
    response.status_code = 400  # 也可以返回HTTP响应状态码，默认是200，可以自行设置其他值
    return HttpResponse(response.content)


'''例2： Django 模板的应用，模板是一个文本，用于分离文档的表现形式和内容'''


def student(request):
    context = {}
    context['test'] = '这是context的字典值：欢迎进入helloworld网页'
    return render(request, 'HelloWorld.html', context)


@csrf_exempt
def sales_page(request):
    context = {}
    return render(request, 'page/index_sales.html', context)


@csrf_exempt
def linkiee_page(request):
    context = {}
    return render(request, 'page/index_linkiee.html', context)

@csrf_exempt
def links_page(request):
    context = {}
    return render(request, 'page/index_links.html', context)