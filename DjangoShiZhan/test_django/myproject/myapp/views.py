from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse


def index(request):
    return HttpResponse('<h1>hello world</h1>')


def test(request):
    hi = 'Hello, the world is beautiful'
    test = 'This is a test page, dymanic page showed normally, test passed'
    return render(request, 'test.html', {'hi': hi, 'test': test})


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'test' and password == '123':
            return redirect('/test/')
        else:
            return render(request, 'login.html', {'error': 'username or password error!'})


def hello(request):
    return render(request, 'hello.html')


def ny(request, year, month):
    year1 = str(year) + '年'
    month1 = str(month) + '月'
    return render(request, 'ny.html', {'year': year1, 'month': month1})


def name(request, username):
    if username == 'redirectny':
        return redirect(reverse('ny', args=(2019,6,)))
    else:
        welcome = 'Welcome ' + username
        return render(request, 'name.html', {'welcome': welcome})


def template_test(request):
    v_list = ['程序员', '产品经理', '产品销售', '架构师']
    v_dic = {'name': '张三', 'age': 16, 'love': '编程'}

    class coder(object):
        def __init__(self, name, language, hair):
            self.name = name
            self.language = language
            self.hair = hair

        def hope(self):
            return f'{self.name} 的希望是程序少出 bug，工作少加班！'

    zhang = coder('张三', 'python', '多')
    li = coder('李四', 'php', '不多不少')
    wang = coder('王五', 'C#', '少')
    coders = [zhang, li, wang]

    return render(request, 'test_template.html', {'v_list': v_list, 'v_dic': v_dic, 'coders': coders})


def test_filter(request):
    vhair = 'fewhair'
    return render(request, 'test_filter.html', {'hair': vhair})


def test_for(request):
    v_list = ['Programmer', 'Product manager', 'Product sales', 'Architect', 'Boss', 'Employee']
    return render(request, 'test_for.html', {'vlist': v_list})


def test_tag(request):
    return render(request, 'test_tag.html')


def test_inclusion_tag(request):
    return render(request, 'test_inclusion_tag.html')


def mother_test(request):
    return render(request, 'inhert_base.html')
