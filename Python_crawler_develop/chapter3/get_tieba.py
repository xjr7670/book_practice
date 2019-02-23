#-*- coding:utf-8 -*-

import re
import csv

with open('tieba.txt', encoding='utf-8') as f:
    source = f.read()

result_list = []
username_list = re.findall('username="(.*?)"', source, re.S)
content_list = re.findall('clearfix" style="display:;">(.*?)<', source, re.S)
print(len(username_list))
print(len(content_list))
for i in range(len(username_list)):
    result = {'username': username_list[i],
              'content': content_list[i]}
    result_list.append(result)

with open('tieba.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['username', 'content'])
    writer.writeheader()
    writer.writerows(result_list)