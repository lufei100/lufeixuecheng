from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from api import models
from api.utils.auth.api_view import AuthAPIView
from api.utils.exception import PricePolicyDoesNotExist
from pool import POOL
import json
from django.conf import settings

import redis
CONN = redis.Redis(connection_pool=POOL)

class ShoppingCarView(AuthAPIView,APIView):

    def get(self,request,*args,**kwargs):
        """
        查看购物车
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        course = CONN.hget(settings.LUFFY_SHOPPING_CAR,request.user.id)
        print('c',course)
        course_dict = json.loads(course.decode('utf-8'))
        # return Response(course_dict)
        return Response(course_dict)

    def post(self,request,*args,**kwargs):
        """
        获取课程ID和价格策略ID，放入redis
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000,'msg':None}
        print(request.data)
        try:
            course_id = request.data.get('course_id')
            price_policy_id = request.data.get('price_policy_id')
            # 1. 获取课程
            course_obj = models.Course.objects.get(id=course_id)

            # 2. 获取当前课程的所有价格策略: id, 有效期，价格
            price_policy_list = []
            flag = False
            price_policy_objs = course_obj.price_policy.all()
            print('price_policy_objs',price_policy_objs)
            for item in price_policy_objs:
                print(item.id,price_policy_id,type(item.id),type(price_policy_id))
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
            print(course_dict)
            # a. 获取当前用户购物车中的课程 car = {1: {,,,}, 2:{....}}
            # b. car[course_obj.id] = course_dict
            # c. conn.hset('luffy_shopping_car',request.user.id,car)
            nothing = CONN.hget(settings.LUFFY_SHOPPING_CAR,request.user.id)
            print('n',nothing)
            if not nothing:
                data = {course_obj.id: course_dict}
            else:
                data = json.loads(nothing.decode('utf-8'))
                data[course_obj.id] = course_dict

            CONN.hset(settings.LUFFY_SHOPPING_CAR,request.user.id, json.dumps(data))

        except ObjectDoesNotExist as e:
            ret['code'] = 1001
            ret['msg'] = "课程不存在"
        except PricePolicyDoesNotExist as e:
            ret['code'] = 1002
            ret['msg'] = "价格策略不存在"
        except Exception as e:
            ret['code'] = 1003
            ret['msg'] = "添加购物车异常"

        return Response(ret)
    '''
    conn = {
        'LUFFY_SHOPPING_CAR':{
            'user_id':{
                'course_id':{
                    'id': course_obj.id,
                    'img': course_obj.course_img,
                    'title': course_obj.name,
                    'price_policy_list': price_policy_list,
                    'default_policy_id': price_policy_id
                }
            }
        }
    }'''
    def delete(self,request,*args,**kwargs):
        ret = {'code':'1000'}
        try:
            course_id = request.data.get('course_id')
            user_dict_str = CONN.hget(settings.LUFFY_SHOPPING_CAR,request.user.id)
            print(user_dict_str)
            course_dict = json.loads(user_dict_str)
            course_dict.pop(course_id)

            CONN.hset(settings.LUFFY_SHOPPING_CAR,request.user.id,json.dumps(course_dict))
        except Exception:
            ret['code'] = '1001'
            ret['err'] = '删除过了'
        return Response(ret)
    def put(self,request,*args,**kwargs):
        ret = {'code': '1000'}
        course_id = request.data.get('course_id')
        valid_period_id = request.data.get('valid_period_id')
        user_dict_str = CONN.hget(settings.LUFFY_SHOPPING_CAR, request.user.id)
        user_course_dict = json.loads(user_dict_str)
        user_course_dict[course_id]['default_policy_id']=valid_period_id
        CONN.hset(settings.LUFFY_SHOPPING_CAR, request.user.id, json.dumps(user_course_dict))

        return Response(ret)


