from django.views import View
from django.http import JsonResponse
from markdown import markdown
from pyquery import PyQuery
from app.models import Tags, Articles, Cover
from django import forms
from api.views.login import clean_form
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
import random



class AddArticleForm(forms.Form):
    title = forms.CharField(error_messages={'required': '请输入文章标题'})
    content = forms.CharField(error_messages={'required': '请输入文章内容'})
    abstract = forms.CharField(required=False) #不进行为空验证
    cover_id = forms.CharField(required=False) #不进行为空验证

    category = forms.CharField(required=False)
    pwd = forms.CharField(required=False)
    recommend = forms.CharField(required=False)
    status = forms.CharField(required=False)

    #全局钩子 分类 密码
    def clean(self):
        category = self.cleaned_data['category']
        print(category)
        if not category:
            self.cleaned_data.pop('category')

        pwd = self.cleaned_data['pwd']
        if not pwd:
            self.cleaned_data.pop('pwd')


    #文章简介
    def clean_abstract(self):
        abstract = self.cleaned_data['abstract']
        if abstract:
            return abstract
        #截取正文前30个字符
        content = self.cleaned_data['content']
        if content:
            abstract = PyQuery(markdown(content)).text()[:30]
            return abstract

    #文章封面
    def clean_cover_id(self):
        cover_id = self.cleaned_data['cover_id']
        if cover_id:
            return cover_id
        cover_set = Cover.objects.all().values('nid')
        cover_id = random.choices(cover_set)['nid']
        return cover_id
        
class ArticleView(View):
    def post(self, request):
        res = {
            'msg': '发布成功！',
            'code': '412',
            'data': None,
        }
        data = request.data
        data['status'] = 1
        form = AddArticleForm(data)
        if not form.is_valid():
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)
        # 校验通过
        form.cleaned_data['author'] = 'willow'
        form.cleaned_data['source'] = 'willow个人博客'
        article_obj = Articles.objects.create(**form.cleaned_data)
        tags = data.get('tags')
        for tag in tags:
            if tag.isdigit():
                article_obj.tag.add(tag)
            else:
                #先创建，在多对多关联
                tag_obj = Tags.objects.create(title=tag)
                article_obj.tag.add(tag_obj.nid)
        res['code'] = 0
        res['data'] = article_obj.nid
        return JsonResponse(res)



# class ArticleView(View):
#     # 发布文章
#     def post(self, request):
#         res = {
#             'msg': '发布成功',
#             'code': 412,
#             'data':None,
#         }
#         data: dict = request.data
#         title = data.get('title')
#         content = data.get('content')
#         recommend = data.get('recommend')
#         if not title:
#             res['msg'] = '请输入文章标题'
#             return JsonResponse(res)
#         if not content:
#             res['msg'] = '请输入文章内容'
#             return JsonResponse(res)

#         extra = {
#             'title': title,
#             'content': content,
#             'recommend': recommend,
#             'status': 1,
#         }
#         #解析文本内容
#         abstract = data.get('abstract')
#         if not abstract:
#             abstract = PyQuery(markdown(content)).text()[:30]
#         extra['abstract'] = abstract

#         category = data.get('category_id')
#         if category_id:
#             extra['category'] = category

#         cover_id = data.get('cover_id')
#         if cover_id:
#             extra['cover_id'] = cover_id
#         else:
#             extra['cover_id'] = 1

#         pwd = data.get('pwd')
#         if cover_id:
#             extra['pwd'] = pwd

#         #添加文章
#         article_obj = Articles.objects.create(**extra)
#         #标签
#         tags = data.get('tags')
#         if tags:
#             for tag in tags:
#                 if not tag.isdigit():
#                     tag_obj = Tags.objects.create(title=tag)
#                     article_obj.tag.add(tag_obj)
#                 else:
#                     article_obj.tag.add(tag)

#         res['code'] = 0
#         res['data'] = article_obj.nid
#         return JsonResponse(res)
