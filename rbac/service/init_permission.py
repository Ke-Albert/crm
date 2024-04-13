from django.conf import settings


def init_permission(req,user):
    """
    权限和菜单信息初始化，使用时需要在用户登陆成功后调用
    :param req:
    :param user: 成功登陆的用户对象
    :return:
    """
    # 获取用户信息的所有角色的权限，并写入session
    # result=user.roles.all().filter(permissions__url__isnull=False).values('id','role','permissions__url')
    # permissions=[]
    # for item in result:
    #     # {'id': 2, 'role': '董事长', 'permissions__url': 'http://localhost/customer/list/'}
    #     # {'id': 2, 'role': '董事长', 'permissions__url': 'http://localhost/payment/list/'}
    #     # print(item)
    #     if item['permissions__url'] not in permissions:
    #         permissions.append(item['permissions__url'])

    permissions_queryset=user.roles.all().\
        filter(permissions__url__isnull=False).\
        values('permissions__url',
               'permissions__id',
               'permissions__parent__id',
               'permissions__title',
               'permissions__menu__id',
               'permissions__menu__title',
               'permissions__menu__icon').distinct()
    req.session['info'] = {'id': user.id, 'name': user.name}
    menu_dict={}#菜单+能成为菜单的权限
    permission_list=[]#所有的权限信息
    for row in permissions_queryset:
        permission_list.append({'id':row['permissions__id'],'pid':row['permissions__parent__id'],'permissions__url':row['permissions__url']})
        menu_id=row['permissions__menu__id']
        if not menu_id:
            continue
        # menu_dict={
        #     id:{
        #         title:xx,
        #         icon:xx,
        #         children:[
        #             {title:xx,url:xx}
        #         ]
        #     }
        # }
        if menu_id not in menu_dict:
            menu_dict[menu_id]={
                'title':row['permissions__menu__title'],
                'icon': row['permissions__menu__icon'],
                'children':[{'id':row['permissions__id'],'title':row['permissions__title'],'url':row['permissions__url']}]
            }
        else:
            menu_dict[menu_id]['children'].append({'id':row['permissions__id'],'title':row['permissions__title'],'url':row['permissions__url']})
    req.session[settings.PERMISSION_SESSION_KEY]=permission_list
    req.session[settings.MENU_SESSION_KEY]=menu_dict
    print(permission_list)
    print(menu_dict)

    req.session.set_expiry(60 * 60 * 24 * 7)