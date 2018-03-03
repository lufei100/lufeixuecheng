from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework import views
from rest_framework import serializers
from rest_framework.response import Response
from .. import models
from ..serializer.order import OrderSerializer



class OrderView(views.APIView):
	def get(self,request,*args,**kwargs):
		print("==================")
		user_id = request.data.get("account_id",1)
		print(user_id)
		#首先应该获取到用户id
		order_list = models.Order.objects.filter(account_id=user_id).all()
		print(order_list)
		ser = OrderSerializer(instance=order_list,many=True)
		print(ser)
		return Response(ser)


		# for order in order_list:
		# 	print(order)
		# return HttpResponse(order_list)