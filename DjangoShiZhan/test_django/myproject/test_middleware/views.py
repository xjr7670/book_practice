from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    print('test() running...')
    return HttpResponse22('hello World')


class TestTemp(object):
    def __init__(self, response):
        self.response = response

    def render(self):
        return self.response


def test2(request):
    print('test2() running...')
    resp = HttpResponse('hello world, this is test2')
    return TestTemp(resp)
