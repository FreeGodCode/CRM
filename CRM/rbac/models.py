from django.db import models

# Create your models here.
class Permission(models.Model):
    """权限表"""
    title = models.CharField(max_length=32, verbose_name='标题')
    url = models.CharField(max_length=128, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'db_permission'
        verbose_name = '权限'
        verbose_name_plural = verbose_name


class Role(models.Model):
    """角色表"""
    title = models.CharField(max_length=32, verbose_name='角色名称')
    permissions = models.ManyToManyField(to='Permission', verbose_name='拥有的权限', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'db_role'
        verbose_name = '角色'
        verbose_name_plural = verbose_name


class UserInfo(models.Model):
    """用户信息表"""
    name = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    email = models.EmailField()
    roles = models.ManyToManyField(to='Role', verbose_name='所拥有的角色', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'db_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


