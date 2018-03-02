from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import views,viewsets
from api import models
###认证
from rest_framework.authentication import TokenAuthentication,RemoteUserAuthentication
#权限
from rest_framework.permissions import BasePermission
#限流
from rest_framework.throttling import BaseThrottle
# 解析器

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import JSONParser
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning,AcceptHeaderVersioning,BaseVersioning,HostNameVersioning,NamespaceVersioning
# 序列化

from api.serializer import course as serializercourse

###############################登录
class LoginView(views.APIView):
    def get(self, request, *args, **kwargs):
        ret = {
            'code': 1000,
            'data': '老男孩'
        }
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = "*"
        return response

    def post(self, request, *args, **kwargs):
        print(request.POST)
        ret = {
            'code': 1000,
            'user': '老男孩',
            'token': 'c4fd684vda6c8vvfv4d98f'
        }
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = "*"
        return response

    def options(self, request, *args, **kwargs):
        # self.set_header('Access-Control-Allow-Origin', "http://www.xxx.com")
        # self.set_header('Access-Control-Allow-Headers', "k1,k2")
        # self.set_header('Access-Control-Allow-Methods', "PUT,DELETE")
        # self.set_header('Access-Control-Max-Age', 10)

        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'content-type'
        # response['Access-Control-Allow-Headers'] = '*'
        # response['Access-Control-Allow-Methods'] = 'PUT'
        return response



############################################普通课程
class CourseView(views.APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            course = models.CourseDetail.objects.filter(course=pk).first()
            courses = course.CourseDetailSerializers(instance=course, many=False).data
        else:
            course_list = models.Course.objects.all()
            ret = serializercourse.CourseSerializers(instance=course_list, many=True)
            courses = ret.data
            courses = serializercourse.CourseMenuSerializers(instance=course_list, many=True).data
        response = Response(courses)
        response['Access-Control-Allow-Origin'] = "*"
        return response



############################################学位课程
class DegreeCourse(views.APIView):
    def get(self,*args,**kwargs):
        self.dispatch
        dgcourses=models.DegreeCourse.objects.all()
        ret=serializercourse.DegreeCourseSerializers(instance=dgcourses,many=True)
        dgcourses_data=ret.data
        response = Response(dgcourses_data)
        response['Access-Control-Allow-Origin'] = "*"
        print(self.authentication_classes)
        return response


##################################################测试
class TestView(views.APIView):
    # parser_classes = [JSONParser, ]
    def get1(self, *args, **kwargs):
        courselist = models.Course.objects.all()
        cat = models.CourseCategory.objects.filter(pk=2).first()
        courses = [
            {
                'name': 'python高级',
                'course_img': 'http://pic1.win4000.com/wallpaper/2017-12-19/5a387cb8439ea.jpg',
                'sub_category_id': 2,
                'course_type': 0,
                'brief': 'python高手的第一堂课',
                'order': 14,
            }, {
                'name': 'python编程',
                'course_img': 'http://pic1.win4000.com/wallpaper/2017-12-19/5a387cb8439ea.jpg',
                'sub_category_id': 2,
                'course_type': 1,
                'brief': 'python编程的课程',
                'order': 14,
            }, {
                'name': 'python实战',
                'course_img': 'http://pic1.win4000.com/wallpaper/2017-12-19/5a387cb8439ea.jpg',
                'sub_category_id': 2,
                'course_type': 2,
                'brief': '实战课程',
                'order': 14,
            }, ]
        models.Course.objects.bulk_create([models.Course(**item) for item in courses])

        print(courselist)
        return HttpResponse()

    def get(self, *args, **kwargs):
        # course_list= models.Course.objects.all()
        # course_value_list= models.Course.objects.values()
        # # return Response(course_value_list)
        # ret=CourseSerializers(instance=course_list,many=True)
        # print(ret.data)
        # # content=JsonResponse.serialize(ret.data)
        # return Response(ret.data)

        #######################CourseDetail添加内容################################3
        # o1 = models.Course.objects.filter(pk__lt=3)
        # c = models.CourseDetail.objects.filter(pk=3).first()
        # c.recommend_courses=[1,2]
        # print(c.recommend_courses)
        # print(o1)
        # item = {
        #     'pk':1,
        #     'course': c,
        #     'hours': 24,
        #     'course_slogan': '你将熟悉真实企业项目从需求提出到最终实现的全过程',
        #     'video_brief_link': 'https://p.bokecc.com/flash/single/D90C6BABEBFD8C03_DAB725C5977D74A19C33DC5901307461_false_6ADBEB8F508329DC_1/player.swf',
        #     'why_study': '你在Python学习或用其在工作中进行项目开发过程中，是否遇到过以下问题？ 1.	学过N多Python知识点，但没有写过或不知道如何写完整的企业项目 2.	工作中有很多需求涉及把数据库里的数据返回到前端页面，并完成增删改查，自己总是要不断的重复写各种功能差不太多的页面，冥冥中你觉得不应该写重复的代码，如果有个通用的增删改查组件可以容易的嵌入到你的各个页面里该多好 3. 你写的每个项目中涉及的权限需求是怎么实现的？每个用户看到页面不同，可以干的事情不同，是不是把权限跟你的代码写死在一起了？那再开发一个项目，权限功能又再重写一次？能不能搞个通用、万能且热插拔的权限组件呢？ 4.	不知道如何设计可扩展的表结构，不确定自己设计的构架会不会存在大坑 若你对以下任意的问题回答是Yes, then, this is the right course for you !',
        #     'what_to_study_brief': '在本实战项目开发过程中，我们将以教育行业CRM为案例背景，你将穿插学到下面内容',
        #     'career_improvement': '通过此项目掌握了项目从0到1的需求讨论、设计、开发全过程，帮助你不仅只从技术角度关注功能实现，并且还能尝试从业务角度思考如何通过技术工具帮助提高业务效率。另外，你将通过此项目熟练的掌握基于Django的web项目开发技能，日后，完成复杂的前后端交互功能，开发支持多角色使用、细致权限管理的需求对你来讲将只是小case!且在项目学习中，我们带你设计的通用增删改查组件、通用权限组件，是可以直接嵌入到你其它的项目中去的，以后再也不用一遍遍的重写这些常用的功能啦，省下来的时间去找个对象吧。',
        #     'prerequisite': '学习此课程前，请确保你已熟练掌握Python基础语法、面向对象编程、数据库操作、Django各组件的使用、Html/Css/JS/Bootstrap/Jquery知识',
        #     'recommend_courses': [1,2],
        #     'teachers': []
        #
        # }
        # o1=models.CourseDetail(**item).save()
        # print(o1)
        m1 = models.Course.objects.filter(pk=1).first()

        n1 = {'valid_period':7, 'price':9.9, 'content_object':m1}
        n2 = {'valid_period':14, 'price':19.9, 'content_object':m1}
        n3 = {'valid_period':30, 'price':39.9, 'content_object':m1}
        # n2 = models.PricePolicy(valid_period=14, price=19.9, content_object=m1)
        # n3 = models.PricePolicy(valid_period=30, price=39.9, content_object=m1)
        # for i in [n1,n2,n3]:
        #     models.PricePolicy.objects.create(**i)
        print(models.PricePolicy.objects.all())
        # print(m1.price_policy.all())
        # l = [
        #     {'name': 'Alex',
        #      'title': '金角大王',
        #      'signature': 'Do the right thing!',
        #      'brief': 'CrazyEye,MadKing,TriAquae三款开源软件作者，10多年运维+自动化开发经验，曾任职公安部、飞信、Nokia中国、汽车之家等公司，热爱技术、电影、音乐、旅游、妹子！',
        #      'image': 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=884743574,576639025&fm=27&gp=0.jpg'},
        #     {'name': '武Sir',
        #      'title': '银角大王',
        #      'signature': '越是憧憬，越要风雨兼程',
        #      'brief': '多年开发实战经验，先后任职于汽车之家、好大夫在线等多家大型互联网公司。擅长C#,Python,PHP等一大堆语言开发，现任某大型互联网公司高级自动化开发工程师，已精读多个开源软件源码，自行开发过改进版的Tornado WEB框架，讲课风趣幽默，除了长的丑，没啥缺点。',
        #      'image': 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2689199741,2522895067&fm=27&gp=0.jpg'},
        # ]
        # t1 = [models.Teacher(**i) for i in l]
        # models.Teacher.objects.bulk_create(t1)
        # l=models.Teacher.objects.filter(pk__lt=3)
        # cou=models.CourseDetail.objects.filter(pk=3).first()
        # cou.teachers.add(*l)
        # print(cou.teachers)
        # print(cou)
        # cuv = models.Course.objects.filter(course_type=2).all().first()
        # dc={'name':'python编程',
        #     'course_img':'http://pic1.win4000.com/wallpaper/2017-12-19/5a387cb8439ea.jpg',
        #     'brief':'python编程的课程',
        #     'total_scholarship':2000,
        #     'prerequisite':cuv.coursedetail.prerequisite,
        #     # 'teachers':cuv.coursedetail.teachers,
        #     }

        # dco=models.DegreeCourse.objects.first()
        # print(**cuv.coursedetail.teachers.all())
        # l=cuv.coursedetail.teachers.all()
        # dco.teachers.add(*l)
        # print(dco.teachers.all())
        ###########################章
        # cc = models.Course.objects.filter(pk=3).first()
        # c1 = {
        #     'course': cc,
        #     'chapter': 1,
        #     'name': '第一章',
        #     'summary': '第一章简介',
        # }
        # c2 = {
        #     'course': cc,
        #     'chapter': 2,
        #     'name': '第二章',
        #     'summary': '第二章简介',
        # }
        # models.CourseChapter.objects.create(**c1)
        # models.CourseChapter.objects.create(**c2)
        # csl = models.CourseChapter.objects.all()
        # cs = {'chapter': csl[0], 'name': '1.1节', 'order': 1}
        # cs1 = {'chapter': csl[0], 'name': '1.2节', 'order': 4}
        # cs2 = {'chapter': csl[1], 'name': '2.1节', 'order': 1}
        # cs3 = {'chapter': csl[1], 'name': '2.2节', 'order': 4}
        # l = [cs, cs1, cs2, cs3]
        # print(list(models.CourseChapter.objects.values()))
        # for i in l:
        #     models.CourseSection.objects.create(**i)
        # b = models.Course.objects.filter(pk=3).first()
        # l = models.OftenAskedQuestion(content_object=b, question='不是说一般都用php或java开发网站么？',
        #                               answer="亲，那是上个世纪的事情了，now it's Python's world， 越来越多的公司开始选择Python的web框架开发网站，当然还是要说,在PHP and Java在WEB开发方向确实很优秀，特别是PHP,毕竟它是世界上最好的语言嘛。").save()
        #
        # l = models.OftenAskedQuestion(content_object=b, question='2.学完此课程后能达到什么水平？',
        #                               answer="可以自行开发一个“抽屉新热榜”或“虎嗅网”").save()
        #
        # l = models.OftenAskedQuestion(content_object=b, question='3.课程里的课件及源代码是否可以提供？',
        #                               answer="可以提供，且我们不只会提供给你最后一个完成后的项目代码，且在开发过程中，每到一个里程碑阶段，我们就会把代码COPY一份，这样，你可以真正见证一个项目是怎么一步步开发出来的。").save()

        return HttpResponse(666)
