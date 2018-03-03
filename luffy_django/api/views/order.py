from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from rest_framework import views
from rest_framework import serializers
from rest_framework.response import Response
from api.utils.auth.api_view import AuthAPIView
from .. import models
from ..serializer.order import OrderSerializer



class OrderView(AuthAPIView,views.APIView):
	def get(self,request,*args,**kwargs):
		user_id = request.user.id
		#首先应该获取到用户id

		order_list = models.Order.objects.filter(account_id=user_id).all()
		# print([order_list1.orderdetail_set.values('id') for order_list1 in order_list],'----------------->')
		# print([order_list1.orderdetail.values('id') for order_list1 in order_list],'----------------->')
		# order_detail_list = models.OrderDetail.objects.first()
		# print(order_detail_list.content_object)
		# print(order_detail_list.content_object.course_img,'==================')
		# print(type(order_detail_list.content_object),order_detail_list.content_object.name)

		#获取到当前用户所有的订单信息
		# print("order_list",order_list.query)
		# print([(obj.account.username,type(obj.account)) for obj in order_list])
		# print([(obj.status,obj.account.username,obj.account_id) for obj in order_list])
		ser = OrderSerializer(instance=order_list,many=True)

		# 序列化返回订单信息
		return Response(ser.data)
		# return HttpResponse(ser)