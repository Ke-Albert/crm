from django.contrib import admin
from rbac import models

# Register your models here.
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['title','url','menu','alias']
    list_editable = ['url','menu','alias']

admin.site.register(models.Menu)
admin.site.register(models.Permission,PermissionAdmin)
admin.site.register(models.UserInfo)
admin.site.register(models.Role)
