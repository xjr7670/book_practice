# -*- coding:utf-8 -*-

import re

from django.conf import settings
from django.shortcuts import HttpResponse, redirect
from django.utils.deprecation import MiddlewareMixin


class RbacMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request_url = request.path_info
        permission_url = request.session.get(settings.PERMISSION_URL_KEY)
        for url in settings.SAFE_URL:
            if re.match(url, request_url):
                return None
        if request.user.is_superuser:
            return None
        if not permission_url:
            return redirect(settings.LOGIN_URL)
        flag = False

        for perm_group_id, code_url in permission_url.items():
            for url in code_url['urls']:
                url_pattern = "^{0}$".format(url)
                if re.match(url_pattern, request_url):
                    request.session['permission_codes'] = code_url['codes']
                    flag = True
                    break

            if flag:
                return None

            if not flag:
                if settings.DEBUG:
                    info = '<br/>' + '<br/>'.join(code_url['urls'])
                    return HttpResponse('No Authority. please visit : %s' % info)
                else:
                    return HttpResponse('No Authority')
