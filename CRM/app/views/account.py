from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from rbac.utils.init_permission import init_permission
from rbac.models import UserInfo


def login(request):
    """
    登录: /account/login/
    """
    if request.method == 'GET':
        return render(request, 'templages.app.login.html')

    # 获取post表单数据
    user = request.POST.get('user', '')
    pwd = request.POST.get('pwd', '')
    # 验证用户名和密码
    current_user = UserInfo.objects.filter(name=user, password=pwd).first()
    if not current_user:
        return render(request, 'login.html', {'msg': '用户名或密码错误'})

    # 权限初始化
    init_permission(current_user, request)
    # 登录完成,重定向到首页
    return redirect('index.html')

    """
    # 权限信息初始化
    # 根据当前用户信息获取此用户所拥有的所有权限
    # permission_queryset = current_user.roles.all().values('permission__id', 'permission__url')
    # 去重    
    # permission_queryset = current_user.roles.all().values('permission__id', 'permission__url').distinct()
    # 可能含有没有分配权限的情况
    permission_queryset = current_user.roles.filter(permission__isnull=False).values('permission__id', 'permission__url').distinct()
    # 获取权限中所有的url
    # permission_list = []
    # for item in permission_queryset:
    #     permission_list.append(item['permission__url'])
    # 采用列表推导式实现
    permission_list = [item['permission__url'] for item in permission_queryset]
    # 将权限对应的url存入session
    # request.session['login_permission_url_list_key'] = permission_list
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    # return HttpResponse('...')
    # 登录完成,重定向到首页
    return redirect('index.html') 
    """




def register(request):
    """
    注册: /account/register/
    """
    pass


def logout(request):
    """
    退出: /account/logout/
    """
    pass


def resetpwd(request):
    """
    重置密码: /account/resetpwd/
    """
    pass
