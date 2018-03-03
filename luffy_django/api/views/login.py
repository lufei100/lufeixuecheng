from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework import views
from rest_framework import serializers
from rest_framework.response import Response
from .. import models

class LoginView(views.APIView):
    def get(self,request,*args,**kwargs):
        print("=======get==========")
        ret = {
            'code':1000,
            'data':'老男孩'
        }
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = "*"
        return response

    def post(self,request,*args,**kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user_obj = models.Account.objects.filter(username=username,password=password).first()
        if user_obj:
            ret = {
                'code':1000,
                'username':username,
                'token':'71ksdf7913knaksdasd7',
            }
            response = Response(ret)
            response['Access-Control-Allow-Origin'] = "*"
        else:
            ret = {
                'code': 1001,
                'msg': "用户名或密码错误",
            }
            response = Response(ret)
            response['Access-Control-Allow-Origin'] = "*"
        return response

    def options(self, request, *args, **kwargs):
        print("======option==========")
        # self.set_header('Access-Control-Allow-Origin', "http://www.xxx.com")
        # self.set_header('Access-Control-Allow-Headers', "k1,k2")
        # self.set_header('Access-Control-Allow-Methods', "PUT,DELETE")
        # self.set_header('Access-Control-Max-Age', 10)

        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        response['Access-Control-Allow-Methods'] = '*'
        return response

