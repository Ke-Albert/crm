from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from rbac import models
from rbac.forms.user_info import User
from rbac.service.init_permission import init_permission
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

        #权限和菜单信息初始化
        init_permission(req,user)
        return redirect('/customer/list/')
    return render(req, 'login.html', {'form': form})

def login_out(req):
    req.session.clear()

    return redirect('/login/')