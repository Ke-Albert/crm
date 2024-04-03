import re

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleWare(MiddlewareMixin):
    """权限控制中间件"""
    def process_request(self,req):
        """权限控制"""
        # 1.获取当前请求的url
        current_url=req.path_info
        #白名单处理
        for reg in settings.WHITE_URLS:
            if re.match(reg,current_url):
                return

        # 2.获取当前用户session中的权限
        permission_list=req.session.get(settings.PERMISSION_SESSION_KEY)
        if not permission_list:
            return redirect('/login/')

        # 3.权限校验
        flag=False
        for permission in permission_list:
            reg="^%s$" % permission.get('permissions__url')
            print(reg,current_url)
            if re.match(reg,current_url):
                flag=True
                break
        if not flag:
            return HttpResponse('无权访问')
