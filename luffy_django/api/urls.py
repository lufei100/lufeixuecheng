"""luffy_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import login
from .views import news
from .views import commit
from .views import shopping_car
from .views import order


urlpatterns = [
    #用户登录
    url(r'^login/$',login.LoginView.as_view()),
    #深科技
    url(r'^news/$',news.NewsView.as_view()),
    url(r'^news/(?P<pk>\d+)\.(?P<format>[a-z0-9]+)$',news.NewsView.as_view()),
    #评论
    url(r'^comment/$',commit.CommentView.as_view()),
    url(r'^comment/(?P<pk>\d+)\.(?P<format>[a-z0-9]+)$',commit.CommentView.as_view()),
    #购物车
    url(r'shopping_car/$',shopping_car.ShoppingCarView.as_view()),
    #我的订单
    url(r'order/$',order.OrderView.as_view())
]
