#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from api.serializer.course import CourseModelSerializer
from api.serializer.course import CourseDetailModelSerializer


class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        response = {'status': False}
        try:
            pk = kwargs.get('pk')
            if not pk:
                queryset = models.Course.objects.exclude(course_type=2)
                ser = CourseModelSerializer(instance=queryset, many=True)
            else:
                queryset = models.CourseDetail.objects.get(course_id=pk)
                ser = CourseDetailModelSerializer(instance=queryset, many=False)
            response['data'] = ser.data
            response['status'] = True
        except Exception as e:
            response['error'] = str(e)
        return Response(response)
