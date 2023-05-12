# -*- coding:utf-8 -*-
import re

from django.conf import settings


def init_permission(request, user_obj):
    permission_item_list = user_obj.roles.values(
        'permissions__id',
        'permissions__title',
        'permissions__url',
        'permissions__perm_code',
        'permissions__pid_id',
        'permissions__perm_group_id',
        'permissions__perm_group__menu_id',
        'permissions__perm_group__menu__title',
    ).distinct()
    permission_url_list = {}
    permission_menu_list = []

    for item in permission_item_list:
        perm_group_id = item['permissions__perm_group_id']
        url = item['permissions__url']
        perm_code = item['permissions__perm_code']
        if perm_group_id in permission_url_list:
            permission_url_list[perm_group_id]['codes'].append(perm_code)
            permission_url_list[perm_group_id]['urls'].append(url)
        else:
            permission_url_list[perm_group_id] = {'codes': [perm_code],
                                                  'urls': [url,]}

    request.session[settings.PERMISSION_URL_KEY] = permission_url_list

    for item in permission_item_list:
        tpl = {
            'id': item['permissions__id'],
            'title': item['permissions__title'],
            'url': item['permissions__url'],
            'pid_id': item['permissions_pid_id'],
            'menu_id': item['permissions__perm_group__menu_id'],
            'menu_title': item['permissions__perm_group__menu__title']
        }

        # added at chapter15
        perm_group_id = item['permissions__perm_group_id']
        url = item['permissions__url']
        url = re.sub(r'<int:\w+>', '[0-9]+', url)
        url = re.sub(r'<str:\w+>', '[^/]+', url)
        url = re.sub(r'<slug:\w+>', '[-a-zA-Z0-9_]+', url)
        url = re.sub(r'<uuid:\w+>', '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', url)
        url = re.sub(r'<path:\w+>', '.+', url)

        perm_code = item['permissions__perm_code']
        if perm_group_id in permission_url_list:
            permission_url_list[perm_group_id]['codes'].append(perm_code)
            permission_url_list[perm_group_id]['urls'].append(url)
        else:
            permission_url_list[perm_group_id] = {'codes': [perm_code,], 'urls': [url,]}
    request.session[settings.PERMISSION_URL_KEY] = permission_url_list
