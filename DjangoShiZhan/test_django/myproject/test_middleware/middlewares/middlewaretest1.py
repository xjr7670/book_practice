# -*- coding:utf-8 -*-
from django.utils.deprecation import MiddlewareMixin


class Middle1(MiddlewareMixin):
    def process_request(self, request):
        print('中间件1的 process_request() 运行，请求 URL 是：', request.path_info)

    def process_response(self, request, response):
        print('中间件1的 process_response() 运行，状态短语：', response.reason_phrase)
        return response
    
    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('Middleware 1 - process_view running...')
        
    def process_exception(self, request, exception):
        print('Middleware 1 - process_exception running...')
        
    def process_template_response(self, request, response):
        print('Middleware 1 - process_template_response running...')
        return response


class Middle2(MiddlewareMixin):
    def process_request(self, request):
        print('中间件2的 process_request() 运行，请求主机 IP：{} - 端口号：{}'.format(
            request.META.get('REMOTE_ADDR'), request.META.get('SERVER_PORT')
        ))

    def process_response(self, request, response):
        print('中间件2的 process_response() 运行，状态码：', response.status_code)
        return response

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print('Middleware 2 - process_view running...')

    def process_exception(self, request, exception):
        print('Middleware 2 - process_exception running...')

    def process_template_response(self, request, response):
        print('Middleware 2 - process_template_response running...')
        return response