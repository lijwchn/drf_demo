from django.db import models


class BaseModel(models.Model):
    # 删除标识
    is_delete = models.IntegerField(default=0)
    # 创建时间, auto_now_add=True 创建数据时, 自动添加当前时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 修改数据, auto_now=True 修改文件时候, 自动添加当前时间
    update_time = models.DateTimeField(auto_now=True)

    # 定义Meta类
    class Meta:
        abstract = True  # 抽象类, 不在数据库中创建这张表
