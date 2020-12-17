import re

from django.conf import settings
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class CheckPermissionMiddleware(MiddlewareMixin):
    """用户权限信息验证"""

    def process_request(self, request):
        """
        当用户请求刚进来时触发执行
        """
        # 1. 获取当前用户请求的URL
        # 2. 获取当前用户在session中保存的权限列表
        # 3. 权限信息匹配

        # 设置权限白名单列表,让那些不需要任何权限的url跳过权限验证中间件
        # 将白名单配置到配置文件中
        # valid_url_list = [
        #     '/login/',
        #     '/admin/.*',
        # ]

        current_url = request.path_info
        # 匹配白名单
        # for valid_url in valid_url_list:
        for valid_url in settings.VALID_URL_LIST:
            if re.match(valid_url, current_url):
                # 白名单中的url不需要权限验证即可访问
                return None

        # 不在白名单列表中的url进行权限验证
        permission_list = request.session.get('login_permission_url_list_key', '')
        if not permission_list:
            return HttpResponse('未获取用户权限信息,请登录')

        flag = False
        for url in permission_list:
            # 含正则的url,拼接上起始符和结束符
            regex = '^%s$' % url
            # url匹配成功
            if re.match(regex, current_url):
                flag = True
                break

        if not flag:
            # 将权限信息也放到配置文件中
            return HttpResponse('无权访问')

