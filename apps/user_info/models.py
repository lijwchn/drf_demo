from django.db import models
from apps.basic.base_model import BaseTable


# 数据量很少，没有加索引
class UserInfo(BaseTable):
    user_name = models.CharField(max_length=100, verbose_name="用户名")
    user_password = models.CharField(max_length=100, verbose_name="用户密码")
    user_phone = models.CharField(max_length=20, verbose_name="电话")

    class Meta:
        db_table = "user_info"
        verbose_name = "用户表"
