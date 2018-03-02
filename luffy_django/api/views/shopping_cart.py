import redis,json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core import exceptions
from rest_framework import views, viewsets
from api import models
from rest_framework.response import Response
from api.utils.redis_pool import POOL
from api.utils.exception import PricePolicyDoesNotExist
from api.serializer.ShoppingCarSerializer import ShoppingCarSerializer
from luffy_django.settings import LUFFY_REDIS

CONN = redis.Redis(connection_pool=POOL)


class ShoppingCart(views.APIView):
    '''
    get：查看购物车
    post：期望获得数据,添加课程到购物车
        {'course_id':1,'pricpolicy_id':1}
    delete：将课程从购物车删除
        从url拿值'shoppingcar/(?P<pk>\d+)/'
    put：修改课程默认策略
        {'course_id':1,'pricpolicy_id':1}
    '''

    def get(self, request, *args, **kwargs):
        '''

        :param request:
        :param args:
        :param kwargs:

        #CONN.hset(LUFFY_REDIS['LUFFY_SHOPPING_CAR'],'5bd6ge6gd5s5fdf465sd64',{})
        :return:
        '''
        # print(ShoppingCarSerializer(instance=models.PricePolicy.objects.all(), many=True).data)
        my_shoppingcar = CONN.hget(LUFFY_REDIS['LUFFY_SHOPPING_CAR'], '5bd6ge6gd5s5fdf465sd64')
        return Response(json.loads(my_shoppingcar))

    def post(self, request, *args, **kwargs):
        result = {
            'code': 1000,
            'msg': ''
        }
        try:
            # 检验获得数据是否合法
            # 不合法抛出异常
            course_id = request.data.get('course_id')
            pricpolicy_id = request.data.get('pricpolicy_id')
            course_obj = models.Course.objects.get(pk=course_id)
            price_policy_list = course_obj.price_policy.all()
            price_policy_vals = []

            flag = False
            for item in price_policy_list:
                if item.pk == pricpolicy_id:
                    flag = True
                price_policy_vals.append({'id': item.id, 'valid_period': item.get_valid_period_display(), 'price': item.price})
            if not flag:
                # print('价格策略不合法')
                raise PricePolicyDoesNotExist
            # 保存到redis中
            # 3. 课程和价格策略均没有问题，将课程和价格策略放到redis中
            # 课程id,课程图片地址,课程标题，所有价格策略，默认价格策略
            course_dict = {
                'id': course_obj.id,
                'img': course_obj.course_img,
                'title': course_obj.name,
                'price_policy_list': price_policy_vals,
                'default_policy_id': pricpolicy_id
            }
            my_shoppingcar=CONN.hget(LUFFY_REDIS['LUFFY_SHOPPING_CAR'], '5bd6ge6gd5s5fdf465sd64')
            if not my_shoppingcar:
                data = {course_id:course_dict}
            else:
                data = json.loads(my_shoppingcar.decode('utf-8'))
                data[course_id] = course_dict
            CONN.hset(LUFFY_REDIS['LUFFY_SHOPPING_CAR'], '5bd6ge6gd5s5fdf465sd64',json.dumps(data))

        except exceptions.ObjectDoesNotExist:
            print('不是合法请求')
            result['code'] = 1001
            result['msg'] = "课程不合法"

        except PricePolicyDoesNotExist as e:
            print(e)
            result['code'] = 1002
            result['msg'] = "价格策略不存在"
        except Exception as e:
            result['code'] = 1003
            result['msg'] = "添加购物车异常"

        return Response(result)
    def delete(self,request,*args,**kwargs):
        result ={'code':1000,'msg':''}

        try:
            course_id=kwargs.get('pk')
            myshoppingcar=CONN.hget(LUFFY_REDIS['LUFFY_SHOPPING_CAR'], '5bd6ge6gd5s5fdf465sd64')
            if not myshoppingcar:
                raise Exception('购物车是空的')
            myshoppingcar=json.loads(myshoppingcar.decode('utf-8'))
            # if course_id not in myshoppingcar:
            if  myshoppingcar.get(course_id) is None:
                raise Exception('购物车发生错误')
            del myshoppingcar[course_id]
        except Exception as e:
            result['code'] = 1001
            result['msg'] = str(e)
        return Response()

    def put(self,request,*args,**kwargs):
        result = {'code': 1000,'msg':''}
        return Response()