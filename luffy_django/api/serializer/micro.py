#!/usr/bin/env python
# -*- coding:utf-8 -*-

from api import models
from rest_framework import serializers


class MicroModelSerializer(serializers.ModelSerializer):
    """
    课程列表
    """
    class Meta:
        model = models.DegreeCourse
        fields = "__all__"


class MicroDetailModelSerializer(serializers.ModelSerializer):
    """
    课程详细
    """
    course_name = serializers.CharField(source='course.name')
    recommends = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = ['id', 'hours', 'course_slogan', 'video_brief_link', 'why_study', 'what_to_study_brief',
                  'career_improvement', 'prerequisite', 'course_name', 'recommends', ]
        depth = 1

    def get_recommends(self, value):
        course_list = value.recommend_courses.all()
        result = []
        for row in course_list:
            result.append({'id': row.id, 'name': row.name})
        return result
