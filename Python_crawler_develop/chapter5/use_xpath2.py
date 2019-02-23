#-*- coding:utf-8 -*-

from lxml import html

html_str = '''<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
    <div id="test3">
        我左青龙,
        <span id="tiger">
            右白虎,
            <ul>上朱雀,
                <li>下玄武</li>
            </ul>
            老牛在当中，
        </span>
        龙头在胸口。
    </div>
</body>
</html>
'''

selector = html.fromstring(html_str)
content = selector.xpath('//div[@id="test3"]')[0]
info = content.xpath('string(.)')
print(info)