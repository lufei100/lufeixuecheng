from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from api import models
from api.utils.auth.api_view import AuthAPIView
from api.utils.exception import PricePolicyDoesNotExist
import json
from django.conf import settings

import redis
POOL = redis.ConnectionPool(host="123.207.145.15",port=6379)
CONN = redis.Redis(connection_pool=POOL)

class ShoppingCarView(AuthAPIView,APIView):
    authentication_classes = []
    def get(self,request,*args,**kwargs):
        print("查看购物车")
        """
        查看购物车
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        course = CONN.hget(settings.LUFFY_SHOPPING_CAR,1)
        course_dict = json.loads(course.decode('utf-8'))
        return Response(course_dict)

    def post(self,request,*args,**kwargs):
        print("更新购物车")
        """
        获取课程ID和价格策略ID，放入redis
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000,'msg':None}
        try:
            course_id = request.data.get('course_id')
            price_policy_id = request.data.get('price_policy_id')
            # 1. 获取课程
            course_obj = models.Course.objects.get(id=course_id)

            # 2. 获取当前课程的所有价格策略: id, 有效期，价格
            price_policy_list = []
            flag = False
            price_policy_objs = course_obj.price_policy.all()
            for item in price_policy_objs:
                if item.id == price_policy_id:
                    flag = True
                price_policy_list.append({'id':item.id, 'valid_period':item.get_valid_period_display(),'price':item.price})
            if not flag:
                raise PricePolicyDoesNotExist()

            # 3. 课程和价格策略均没有问题，将课程和价格策略放到redis中
            # 课程id,课程图片地址,课程标题，所有价格策略，默认价格策略
            course_dict = {
                'id':course_obj.id,
                'img':course_obj.course_img,
                'title':course_obj.name,
                'price_policy_list':price_policy_list,
                'default_policy_id':price_policy_id
            }

            # a. 获取当前用户购物车中的课程 car = {1: {,,,}, 2:{....}}
            # b. car[course_obj.id] = course_dict
            # c. conn.hset('luffy_shopping_car',request.user.id,car)
            nothing = CONN.hget(settings.LUFFY_SHOPPING_CAR,1)
            if not nothing:
                data = {course_obj.id: course_dict}
            else:
                data = json.loads(nothing.decode('utf-8'))
                data[course_obj.id] = course_dict

            CONN.hset(settings.LUFFY_SHOPPING_CAR,1, json.dumps(data))

        except ObjectDoesNotExist as e:
            ret['code'] = 1001
            ret['msg'] = "课程不存在"
        except PricePolicyDoesNotExist as e:
            ret['code'] = 1002
            ret['msg'] = "价格策略不存在"
        except Exception as e:
            ret['code'] = 1003
            ret['msg'] = "添加购物车异常"

        return Response(data)


