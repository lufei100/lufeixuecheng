from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework import views
from rest_framework import serializers
from rest_framework.response import Response
from . import models


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

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = "__all__"
        depth = 2

class NewsView(views.APIView):
    def get(self,request,*args,**kwargs):
        self.dispatch
        pk = kwargs.get('pk')
        if pk:
            article = models.Article.objects.filter(pk=pk).first()
            ser = NewsSerializer(instance=article,many=False)
            response = Response(ser.data)
            response['Access-Control-Allow-Origin'] = "*"
        else:
            article_list = models.Article.objects.all()
            ser = NewsSerializer(instance=article_list,many=True)
            print("================",ser)
            print("================",ser.data)
            response = Response(ser.data)
            response['Access-Control-Allow-Origin'] = "*"
        return response

    def put(self,request,*args,**kwargs):
        article_id = request.GET.get("article_id")
        agree_num = request.GET.get("agree_num")
        agree_info = request.GET.get("agree_info")
        collect_info = request.GET.get("collect_info")
        collect_num = request.GET.get("collect_num")
        if agree_info:
            agree_msg = models.Article.objects.filter(pk=article_id).update(agree_num=agree_num)
            if agree_msg:
                ret = {"msg":"点赞成功！"}
                response = Response(ret)
                response['Access-Control-Allow-Origin'] = "*"
                return response
        if collect_info:
            collect_msg = models.Article.objects.filter(pk=article_id).update(collect_num=collect_num)
            if collect_msg:
                ret = {"msg":"收藏成功"}
                response = Response(ret)
                response['Access-Control-Allow-Origin'] = "*"
                return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        response['Access-Control-Allow-Methods'] = '*'
        return response


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"
        depth = 2

class CommentView(views.APIView):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get("pk")
        comment_list = models.Comment.objects.filter(article_id=pk).all()
        ser = CommentSerializer(instance=comment_list,many=True)
        response = Response(ser.data)
        response['Access-Control-Allow-Origin'] = "*"
        return response
    def post(self,request,*args,**kwargs):
        """article_id,content,account,"""
        pk = kwargs.get("pk")
        comment_count = request.GET.get("comment_count")
        comment_msg = models.Comment.objects.create(article_id=pk,content=comment_count,account_id=1)
        if comment_msg:
            comment_list = models.Comment.objects.filter(article_id=pk).all()
            ser = CommentSerializer(instance=comment_list, many=True)
            response = Response(ser.data)
            response['Access-Control-Allow-Origin'] = "*"
            return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        response['Access-Control-Allow-Methods'] = '*'
        return response



