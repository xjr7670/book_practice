#-*- coding:utf-8 -*-

from lxml import html

html1 = '''<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
    <div id="test-1">需要的内容</div>
    <div id="test-2">需要的内容2</div>
    <div id="testfault">需要的内容3</div>
    <div id="useless">不需要的内容</div>
</body>
</html>
'''

selector = html.fromstring(html1)
content = selector.xpath('//div[starts-with(@id, "test")]/text()')
for each in content:
    print(each)