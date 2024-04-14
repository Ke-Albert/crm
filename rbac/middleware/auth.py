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
        permission_dict=req.session.get(settings.PERMISSION_SESSION_KEY)
        if not permission_dict:
            return redirect('/login/')

        req.breadcrumb_list=[
            {'title':'首页','url':'/'},
        ]

        # 3.权限校验
        flag=False
        for permission in permission_dict.values():
            id=permission.get('id')
            pid=permission.get('pid')
            palias=permission.get('palias')
            reg="^%s$" % permission.get('permissions__url')
            # print(reg,current_url)
            if re.match(reg,current_url):
                flag=True
                if pid:
                    req.current_id=pid
                    req.breadcrumb_list.extend([
                        {'title':permission_dict[palias]['title'],'url':permission_dict[palias]['permissions__url']},
                        {'title': permission['title'], 'url': permission['permissions__url']},
                    ])
                else:
                    req.current_id=id
                    req.breadcrumb_list.extend([{'title': permission['title'], 'url': permission['permissions__url']}])
                break
        if not flag:
            return HttpResponse('无权访问')
