from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseTable(models.Model):
    # 创建时间, auto_now_add=True 创建数据时, 自动添加当前时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 修改数据, auto_now=True 修改文件时候, 自动添加当前时间
    update_time = models.DateTimeField(auto_now=True)
    creator = models.CharField(verbose_name="创建人", max_length=20, null=True)
    updater = models.CharField(verbose_name="更新人", max_length=20, null=True)

    class Meta:
        abstract = True


class SoftDeleteTable(models.Model):
    is_delete = models.IntegerField(default=0, verbose_name="删除标识")

    class Meta:
        abstract = True


# class UserInfo(BaseTable, SoftDeleteTable):
#     class Meta:
#         verbose_name = "用户注册信息表"
#         db_table = "user_info"
#
#     level_type = (
#         (0, '普通用户'),
#         (1, '管理员'),
#     )
#     username = models.CharField('用户名', max_length=20, unique=True, null=False)
#     password = models.CharField('登陆密码', max_length=100, null=False)
#     email = models.EmailField('用户邮箱', unique=True, null=False)
#     level = models.IntegerField('用户等级', choices=level_type, default=0)
