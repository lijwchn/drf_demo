from django.urls import path
from .views import DeviceGenericAPIView

urlpatterns = [
    path("devices", DeviceGenericAPIView.as_view()),
]
