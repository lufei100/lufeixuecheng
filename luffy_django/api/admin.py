from django.contrib import admin
from . import models

admin.site.register(models.Account)
admin.site.register(models.UserAuthToken)
admin.site.register(models.ArticleSource)
admin.site.register(models.Article)
admin.site.register(models.Comment)
admin.site.register(models.Collection)
