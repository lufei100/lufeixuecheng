from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from api import models

class ShoppingCarSerializer(ModelSerializer):

    class Meta:
        model = models.Course
        fields = "__all__"
        # fields = ['user', 'pwd', 'ut']
        depth = 0