from django import template

#注册
register = template.Library()
#自定义过滤器
# @register.filter
# def add(item):
#     return int(item) + 1

@register.inclusion_tag('my_tag/headers.html') #返回一个页面
def banner(menu_name, article=None):
    img_list = [
        "http://127.0.0.1:8000/static/jpg/1.jpg",
        "http://127.0.0.1:8000/static/jpg/2.jpg",
        "http://127.0.0.1:8000/static/jpg/3.jpg",
        "http://127.0.0.1:8000/static/jpg/4.jpg",
        "http://127.0.0.1:8000/static/jpg/5.jpg",
        "http://127.0.0.1:8000/static/jpg/6.jpg",
        "http://127.0.0.1:8000/static/jpg/7.jpg",
        "http://127.0.0.1:8000/static/jpg/8.jpg",
    ]
    if  article:
        #文章
        cover = article.cover.url.url
        img_list = [cover]
        pass
    return {"img_list": img_list}