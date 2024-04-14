from django.db import models


# Create your models here.
class UserInfo(models.Model):
    """用户表"""
    name = models.CharField(verbose_name='name', max_length=32)
    password = models.CharField(verbose_name='pwd', max_length=64)
    email = models.CharField(verbose_name='email', max_length=32)
    roles = models.ManyToManyField(verbose_name='owned roles', to='Role', blank=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    """一级菜单表"""
    title = models.CharField(verbose_name='title', max_length=32, unique=True)
    icon = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.title


class Permission(models.Model):
    """权限表"""
    title = models.CharField(verbose_name='title', max_length=32)
    url = models.CharField(verbose_name='reg url', max_length=128)
    parent = models.ForeignKey(verbose_name='parent permission', to='Permission', null=True, blank=True,
                               on_delete=models.RESTRICT)
    menu = models.ForeignKey(verbose_name='menu', to='Menu', null=True, blank=True, on_delete=models.RESTRICT)
    alias=models.CharField(verbose_name='url alias',max_length=32,unique=True,null=True,blank=True)

    def __str__(self):
        return self.title


class Role(models.Model):
    """角色表"""
    role = models.CharField(verbose_name='role', max_length=32)
    permissions = models.ManyToManyField(verbose_name='owned permissions', to='Permission', blank=True)

    def __str__(self):
        return self.role
