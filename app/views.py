from django.shortcuts import render,HttpResponse, redirect
from django.http import JsonResponse
from app.utils.random_code import random_code
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.contrib import auth
from django.contrib.auth.models import User
from app.models import UserInfo
from app.models import Articles, Tags, Cover


# Create your views here.

def index(request):
    article_list = Articles.objects.filter(status=1).order_by('-change_date')
    qianduan_list = Articles.objects.filter(category=5)[:6]
    houduan_list = article_list.filter(category=2)[:6]
    return render(request, 'index.html', locals())

def article(request, nid):
    article_query = Articles.objects.filter(nid=nid)
    if not article_query:
        return redirect('/')
    article = article_query.first()
    return render(request, 'article.html',locals())


def sort(request):
    article_list = Articles.objects.filter(status=1)
    qianrushi_list = article_list.filter(category=4).order_by('-change_date')
    python_list = article_list.filter(category=5).order_by('-change_date')
    moyu_list = article_list.filter(category=6).order_by('-change_date')
    return render(request, 'sort.html', locals())

#登陆失败的可复用代码
def clean_form(form):
    err_dict:dict = form.errors
    #拿到所有错误的字段名字
    err_name = list(err_dict.keys())[0]
    #拿到第一个字段的第一个错误信息
    err_msg = err_dict[err_name][0]
    return err_msg, err_name

def login(request):
    return render(request, 'login.html')


def get_random_code(request):
    data, valid_code = random_code()
    request.session['valid_code'] = valid_code
    return HttpResponse(data)

def sign(request):
    return render(request, 'sign.html')

def logout(request):
    auth.logout(request)

    return redirect('/')

def backend(request):
    if not request.user.username:
        return redirect('/')
    return render(request, 'backend/backend.html', locals())

def add_article(request):
    # 拿到所有的分类，标签
    tag_list = Tags.objects.all()
    #拿到所有文章的封面
    cover_list = Cover.objects.all()
    c_l = []
    for cover in cover_list:
        c_l.append({
            'url': cover.url.url,
            'nid': cover.nid,
        })

    return render(request, 'backend/add_article.html', locals())

def edit_avatar(request):
    return render(request, 'backend/edit_avatar.html', locals())

def reset_password(request):
    return render(request, 'backend/reset_password.html', locals())

def edit_article(request, nid):
    article_obj = Articles.objects.get(nid=nid)
    return render(request, 'backend/add_article.html', locals())

def about(request):
    return render(request, 'about.html', locals())

def message(request):
    return render(request, 'message.html', locals())