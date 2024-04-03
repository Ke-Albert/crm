from django.db import models


# Create your models here.
class UserInfo(models.Model):
    """用户表"""
    name = models.CharField(verbose_name='name', max_length=32)
    password=models.CharField(verbose_name='pwd',max_length=64)
    email=models.CharField(verbose_name='email',max_length=32)
    roles=models.ManyToManyField(verbose_name='owned roles',to='Role',blank=True)

    def __str__(self):
        return self.name

class Permission(models.Model):
    """权限表"""
    title=models.CharField(verbose_name='title',max_length=32)
    url=models.CharField(verbose_name='reg url',max_length=128)

    is_menu=models.BooleanField(verbose_name='是否可做菜单',default=False)
    icon=models.CharField(max_length=32,null=True,blank=True)
    def __str__(self):
        return self.title

class Role(models.Model):
    """角色表"""
    role=models.CharField(verbose_name='role',max_length=32)
    permissions=models.ManyToManyField(verbose_name='owned permissions',to='Permission',blank=True)

    def __str__(self):
        return self.role