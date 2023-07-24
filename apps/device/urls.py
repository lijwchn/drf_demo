from django.urls import path
from .views1 import DeviceGenericAPIView

urlpatterns = [
    # 下面根据id进行查询时，需要配置如下这个路由
    # path("devices/<int:id>", DeviceGenericAPIView.as_view()),
    path("devices", DeviceGenericAPIView.as_view()),
]
