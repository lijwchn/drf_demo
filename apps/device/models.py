from django.db import models
from apps.basic.base_model import BaseTable, SoftDeleteTable


# 数据量很少，没有加索引
class Device(BaseTable, SoftDeleteTable):
    code = models.CharField(max_length=100, verbose_name="设备编码")
    name = models.CharField(max_length=100, verbose_name="设备名称")
    device_type = models.CharField(max_length=100, verbose_name="设备类型")
    purchase_time = models.DateField(verbose_name="购买时间")

    class Meta:
        db_table = "device"
        verbose_name = "设备表"
