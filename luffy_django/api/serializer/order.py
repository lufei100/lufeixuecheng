from rest_framework import serializers
from .. import models

class OrderSerializer(serializers.ModelSerializer):
	order_detail = serializers.SerializerMethodField()
	status = serializers.SerializerMethodField()
	class Meta:
		model = models.Order
		fields = ['order_number','date','order_detail','status']

	def get_order_detail(self,obj):
		order_detail_list = obj.orderdetail_set.all()
		# print('================>.>',order_detail_list.first().content_object.course_img)
		data_list = []
		for item in order_detail_list:
			data_list.append({
				"id":item.id,
				"original_price":item.original_price,
				"valid_period_display":item.valid_period_display,
				"course_img":item.content_object.course_img,
				"course_name":item.content_object.name
			})

		return data_list
	def get_status(self,obj):
		# choice字段专用
		return obj.get_status_display()

