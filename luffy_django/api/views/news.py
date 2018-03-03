from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework import views
from rest_framework import serializers
from rest_framework.response import Response
from .. import models
from ..serializer.news import NewsSerializer




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