from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework import views
from rest_framework import serializers
from rest_framework.response import Response
from .. import models
from ..serializer.commit import CommentSerializer

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