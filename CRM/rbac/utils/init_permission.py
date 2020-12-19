from django.conf import settings

def init_permission(current_user, request):
    """
    用户权限初始化
    :param current_user:
    :param request:
    """
    # 权限信息初始化
    # 根据当前用户信息获取此用户所拥有的所有权限
    # permission_queryset = current_user.roles.all().values('permission__id', 'permission__url')
    # 去重
    # permission_queryset = current_user.roles.all().values('permission__id', 'permission__url').distinct()
    # 可能含有没有分配权限的情况
    permission_queryset = current_user.roles.filter(permission__isnull=False).values(
        'permission__id',
        'permission__title',
        'permission__url',
        'permission__pid_id',
        # 'permission__is_menu',
        # 'permission__icon'
        'permission__menu_id',
        'permission__menu__title',
        'permission__menu__icon',
    ).distinct()

    # 获取权限中所有的url + 菜单信息
    # menu_list = []
    menu_dict = {}
    permission_list = []
    for item in permission_queryset:
        # permission_list.append(item['permission__url'])
        permission_list.append({
            'id': item['permission__id'], 'url': item['permission__url'], 'pid': item['permission__pid_id']
        })
        # if item['permission__is_menu']:
            # temp = {
            #     'title': item['permission__title'],
            #     'icon': item['permission__icon'],
            #     'url': item['permission__url'],
            # }
            # menu_list.append(temp)
        # menu_id默认为null
        menu_id = item['permission__menu_id']
        # menu_id == null
        if not menu_id:
            continue

        node = {'id': item['permission__id'], 'title': item['permission__title'], 'url': item['permission__url']}
        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append(node)
        else:
            menu_dict[menu_id] = {
                'title': item['permission__menu__title'],
                'icon': item['permission__menu__icon'],
                'children': [node, ]
            }

    # 采用列表推导式实现
    # permission_list = [item['permission__url'] for item in permission_queryset]
    # 将权限对应的url存入session
    request.session[settings.PERMISSION_URL_SESSION_KEY] = permission_list

    # 将菜单信息存入session
    # request.session[settings.MENU_SESSION_KEY] = menu_list
    request.session[settings.MENU_SESSION_KEY] = menu_dict