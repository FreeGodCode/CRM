import re

from django.conf import settings
from django.template import Library

register = Library()


# inclusion_tag的使用:侧边菜单
@register.inclusion_tag('rbac/static_menu.html')
def static_menu(request):
    """
    创建一级菜单
    :return:
    """
    """
    <div class="static_menu">
    {% for item in menu_list %}
        <a href="{{ item.url }}" class="active">
            <span class="icon-wrap"><i class="fa {{ item.icon }}"></i></span>{{ item.title }}
        </a>
    {% endfor %}
</div>
    """
    menu_list = request.session[settings.MENU_LIST_SESSION_KEY]
    return {'menu_list': menu_list}


@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):
    """
    创建二级菜单
    :return:
    """
    menu_dict = request.session[settings.MENU_SESSION_KEY]
    # 对字典中的key进行排序
    key_list = sorted(menu_dict)
    ordered_dict = OrderedDict()
    for key in key_list:
        val = menu_dict[key]
        val['class'] = 'hide'
        for per in val['children']:
            regex = '^%s$' % (per['url'], )
            if re.match(regex, request.path_info):
                per['class'] = 'active'
                val['class'] = ''
        ordered_dict[key] = val

    return {'menu_dict': ordered_dict}