#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin, ModelViewSet

from rest_framework.response import Response
from api import models
from api.serializer.article import ArticleModelSerializer


class ArticleView(ViewSetMixin, APIView):
    def get(self, request, *args, **kwargs):
        response = {'status': False}
        try:
            queryset = models.Article.objects.all()
            ser = ArticleModelSerializer(instance=queryset, many=True)
            response['data'] = ser.data
            response['status'] = True
        except Exception as e:
            response['error'] = str(e)
        return Response(response)

    def retrieve(self, request, pk):
        response = {'status': False}
        try:
            queryset = models.Article.objects.get(pk)
            ser = ArticleModelSerializer(instance=queryset, many=False)
            response['data'] = ser.data
            response['status'] = True
        except Exception as e:
            response['error'] = str(e)
        return Response(response)
