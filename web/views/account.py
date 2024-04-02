from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from rbac import models
from rbac.forms.user_info import User
def login(req):
    if req.method=='GET':
        form=User()
        return render(req,'login.html',{'form':form})

    form =User(data=req.POST)
    if form.is_valid():
        user=models.UserInfo.objects.filter(**form.cleaned_data).first()
        if not user:
            form.add_error('password', '用户名或密码错误')
            return render(req, 'login.html', {'form': form})
            # cookie and session

        print('#######')
        # 获取用户信息的所有角色的权限，并写入session
        # result=user.roles.all().filter(permissions__url__isnull=False).values('id','role','permissions__url')
        # permissions=[]
        # for item in result:
        #     # {'id': 2, 'role': '董事长', 'permissions__url': 'http://localhost/customer/list/'}
        #     # {'id': 2, 'role': '董事长', 'permissions__url': 'http://localhost/payment/list/'}
        #     # print(item)
        #     if item['permissions__url'] not in permissions:
        #         permissions.append(item['permissions__url'])

        permissions=user.roles.all().filter(permissions__url__isnull=False).values('permissions__url').distinct()
        req.session['info'] = {'id': user.id, 'name': user.name}
        req.session[settings.PERMISSION_SESSION_KEY]=list(permissions)
        req.session.set_expiry(60 * 60 * 24 * 7)
        return redirect('/customer/list/')
    return render(req, 'login.html', {'form': form})

def login_out(req):
    req.session.clear()

    return redirect('/login/')