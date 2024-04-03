import re

from django.conf import settings
from django.template import Library

register=Library()

@register.inclusion_tag('menu.html')
def menu(request):
    menu_list=request.session.get(settings.MENU_SESSION_KEY)
    for item in menu_list:
        reg="^%s$" % item['url']
        if re.match(reg,request.path_info):
            item['class']='active'
    return {'menu_list':menu_list}