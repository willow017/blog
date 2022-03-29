from django.utils.deprecation import MiddlewareMixin
import json


# 解析post请求的数据
class md1(MiddlewareMixin):
    #请求中间件
    def process_request(self, request):
        if request.method == 'POST' and request.META.get('CONTENT_TYPE') == 'application/json':
            data = json.loads(request.body, encoding='utf8')
            request.data = data

    #响应中间件
    def process_response(self, request, response):
       # print('响应')
        return response