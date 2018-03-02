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




#老郭上传的购物车相关，随便删除
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import APIException
from api.utils.exception import PricePolicyDoesNotExist
from django.core.exceptions import ObjectDoesNotExist

from django.conf import settings
import json
import redis
from pool import POOL

class MyAuthenticate(BaseAuthentication):
    def authenticate(self, request):
        token=request.query_params.get("token")
        print(token)
        obj=models.UserAuthToken.objects.filter(token=token).first()
        print(obj)
        if obj:
            return (obj.user.username,obj)
        raise APIException("用户认证失败")


CONN = redis.Redis(connection_pool=POOL)

class ShoppingCarView(views.APIView):
    authentication_classes = [MyAuthenticate]

    def post(self,request,*args,**kwargs):
        """
        获取课程ID和价格策略ID，让入redis
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000,'msg':None}#最后如果报错需要返回的值
        try:
            course_id = request.data.get("course_id")#获取课程id
            price_policy_id = request.data.get("price_policy_id")#获取策略id
            # 获取课程
            course_obj = models.Course.objects.get(id=course_id)
            # 获取当前课程的所有价格策略：id.，有效期，价格
            price_policy_list = []
            flag = False
            price_policy_objs = course_obj.price_policy.all()#??
            for item in price_policy_objs:
                if item.id == price_policy_id:
                    flag = True
                price_policy_list.append({
                    'id':item.id,
                    'valid_period':item.get_valid_period_display(),
                    "price":item.price
                })
            if not flag:
                raise PricePolicyDoesNotExist()
            # 课程和价格策略均没有问题，将课程和价格策略方到redis中
            #课程id，课程的图片，标题，所有的价格策略和默认的价格策略
            course_dict = {
                'id':course_obj.id,#课程的id
                'img':course_obj.course_img,#课程图片
                'title':course_obj.name,#课程标题
                'price_policy_list':price_policy_list, # 所有的价格策略
                'default_policy_id':price_policy_id # 默认价格策略#
            }
            print(course_dict,'99999999999999999')

            # 获取购物车中的课程
            #
            nothing = CONN.hget(settings.LUFFY_SHOPPING_CAR,request.user.id)
            if not nothing:
                data = {course_obj.id:course_dict}
            else:
                data = json.loads(nothing.decode('utf-8'))
                data[course_obj.id] = course_dict
            CONN.hset(settings.LUFFY_SHOPPING_CAR,request.user.id,json.dumps(data))
            aaa = CONN.hget(settings.LUFFY_SHOPPING_CAR,request.user.id)
            print(aaa,'99999999999999999999')

        except ObjectDoesNotExist as e:
            ret['code'] = 1001
            ret['code'] = '不存在的熊得'
        except PricePolicyDoesNotExist as e:
            ret['code'] = 1002
            ret['msg'] = "价格策略不存在啊"
        except Exception as e:
            ret['code'] = 1003
            ret['msg'] = "添加购物车错误了呀"
        return Response(ret)


