# -*- coding:utf-8 -*-

import socket


def index(url):
    with open('index.html', 'r', encoding='utf-8') as f:
        rd = f.read()
        rd = rd.replace('$@index$@', 'Home')
    return bytes(rd, encoding='utf-8')


def test(url):
    with open('test.html', 'r', encoding='utf-8') as f:
        rd = f.read()
        rd = rd.replace('$@test$@', 'test')
    return bytes(rd, encoding='utf-8')


def fun404(url):
    ret = '<h1>not found!</h1>'
    return bytes(ret, encoding='utf-8')


url_func = [
    ('/index/', index),
    ('/test/', test),
]

sk = socket.socket()
sk.bind(('127.0.0.1', 8000))
sk.listen()
print('socket server is running ...')

while True:
    conn, addr = sk.accept()
    print('\nThe request ip address is : ', addr)
    data = conn.recv(1024)
    print(data)
    if not data:
        continue
    data_str = str(data, encoding='utf-8')
    line = data_str.split('\r\n')
    v1 = line[0].split()
    url = v1[1]
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    func = None
    for i in url_func:
        if i[0] == url:
            func = i[1]
            break

    if func:
        func = func
    else:
        func = fun404

    rep = func(url)
    conn.send(rep)
    conn.close()
