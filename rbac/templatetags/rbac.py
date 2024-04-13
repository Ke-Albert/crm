import re
from collections import OrderedDict

from django.conf import settings
from django.template import Library

register = Library()


@register.inclusion_tag('rbac/static_menu.html')
def static_menu(request):
    """
    创建一级菜单
    :return:
    """
    menu_list = request.session[settings.MENU_SESSION_KEY]
    return {'menu_list': menu_list}


@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):
    menu_dict = request.session.get(settings.MENU_SESSION_KEY)
    ordered_dict = OrderedDict()
    current_url = request.path_info
    for key in sorted(menu_dict.keys()):
        menu_dict[key]['class'] = 'hide'
        ordered_dict[key] = menu_dict[key]
        for row in ordered_dict[key]['children']:
            # regex = '^%s$' % row['url']
            # if re.match(regex, current_url):
            if row['id']==request.current_id:
                row['class'] = 'active'
                ordered_dict[key]['class'] = ''
    return {'menu_dict': ordered_dict}
