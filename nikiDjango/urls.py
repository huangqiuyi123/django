"""nikiDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views
from App import tests
from App import Api

# 添加路由地址

urlpatterns = [
    path('admin/', admin.site.urls),
    path('123/', views.student),  # 访问视图的student对象，student对象指向的是HelloWorld.html
    path('122/', views.hello),  # 访问的是视图的hello对象，hello对象使用的是HttpResponse直接返回的值
    path('111/', tests.testdb),  # 访问的是TestModel应用的tests文件下的testdb对象
    path('queryById/', tests.querry),  # 访问的是TestModel应用的tests文件下的querry对象
    path("addProduct/", Api.MainRequests.addProduct),
    path("queryPruductList/", Api.MainRequests.productList),

    path('sales/', views.sales_page),
    path('linkiee/', views.linkiee_page),
    path('links/', views.links_page),

]
