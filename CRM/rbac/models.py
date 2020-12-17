from django.db import models

# Create your models here.
# class Permission(models.Model):
#     """权限表"""
#     title = models.CharField(max_length=32, verbose_name='标题')
#     url = models.CharField(max_length=128, verbose_name='URL')
#     is_menu = models.BooleanField(default=False, verbose_name='是否可以做菜单')
#     icon = models.CharField(max_length=32, verbose_name='图标', blank=True, null=True)

    # def __str__(self):
    #     return self.title
    #
    # class Meta:
    #     db_table = 'db_permission'
    #     verbose_name = '权限'
    #     verbose_name_plural = verbose_name


class Role(models.Model):
    """角色表"""
    title = models.CharField(max_length=32, verbose_name='角色名称')
    permissions = models.ManyToManyField(to='Permission', verbose_name='拥有的权限', blank=True)

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
        db_table = 'db_userinfo'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Menu(models.Model):
    """菜单表"""
    title = models.CharField(max_length=32, verbose_name='一级菜单名称')
    icon = models.CharField(max_length=32, verbose_name='图标', null=True, blank=True)

    def __str__(self):
        return self.title


# 对应的Permissioin表结构修改,添加foreignkey
class Permission(models.Model):
    """权限表"""
    title = models.CharField(max_length=32, verbose_name='标题')
    url = models.CharField(max_length=32, verbose_name='含正则的URL')
    menu = models.ForeignKey(to='Menu', verbose_name='所属菜单', null=True, blank=True, help_text='null表示不是菜单,非null表示是二级菜单', on_delete=models.CASCADE)
    # 自关联
    pid = models.ForeignKey(to='Permission', verbose_name='关联的权限', null=True, blank=True, related_name='parents', help_text='对于非菜单权限,需要选择一个可以成为菜单的权限,用户做默认展开和选中菜单', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'db_permission'
        verbose_name = '权限'
        verbose_name_plural = verbose_name