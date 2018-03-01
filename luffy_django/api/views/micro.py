#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from api.serializer.micro import MicroModelSerializer
from api.serializer.micro import MicroDetailModelSerializer


class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        response = {'status': False}
        try:
            pk = kwargs.get('pk')
            if not pk:
                queryset = models.DegreeCourse.objects.all()
                ser = MicroModelSerializer(instance=queryset, many=True)
            else:
                queryset = models.CourseDetail.objects.get(course_id=pk)
                ser = MicroDetailModelSerializer(instance=queryset, many=False)
            response['data'] = ser.data
            response['status'] = True
        except Exception as e:
            response['error'] = str(e)
        return Response(response)
