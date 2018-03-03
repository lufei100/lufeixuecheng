from django.conf.urls import url
from .views import auth
from .views import course
from .views import price
from .views import article
from .views import shopping_car
# from .views import payment
# from .views import order
# from .views import alipay

urlpatterns = [
    url(r'^auth/$', auth.AuthView.as_view()),
    url(r'^courses/$', course.CourseView.as_view()),
    url(r'^courses/(?P<pk>\d+)/$', course.CourseView.as_view()),
    url(r'^price_policy/(?P<course_id>\d+)/$', price.PricePolicyView.as_view()),
    url(r'^article/$', article.ArticleView.as_view({'get': 'get'})),
    url(r'^article/(?P<pk>\d+)/$', article.ArticleView.as_view({'get': 'retrieve'})),

    url(r'^shopping_car/$', shopping_car.ShoppingCarView.as_view()),
    url(r'^shopping_car/(?P<pk>\d+)/$', shopping_car.ShoppingCarView.as_view()),

    # url(r'^shop_car/$', shopping_car.ShoppingCarView.as_view({'get': 'get', 'post': 'post'})),
    # url(r'^shop_car/(?P<pk>\d+)/$', shopping_car.ShoppingCarView.as_view({'delete': 'delete', 'put': "put"})),
    # url(r'^payment/$', payment.PaymentView.as_view()),
    # url(r'^order/$', order.PayOrderView.as_view()),
    # url(r'^alipay/$', alipay.AlipayView.as_view()),
]
