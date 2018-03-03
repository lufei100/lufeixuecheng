from rest_framework import serializers
from .. import models

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = "__all__"
        depth = 2