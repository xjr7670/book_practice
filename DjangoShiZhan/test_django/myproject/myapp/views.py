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
