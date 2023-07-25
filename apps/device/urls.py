from django.urls import path
from .views import GetUpdateDeviceById, GetCreateDeleteDevice

urlpatterns = [
    # 下面根据id进行查询时，需要配置如下这个路由
    path("devices/<int:id>", GetUpdateDeviceById.as_view()),
    path("devices", GetCreateDeleteDevice.as_view()),
    path("devices/page/<int:page>/<int:page_size>", GetCreateDeleteDevice.as_view()),
]
