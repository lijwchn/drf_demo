from django.urls import path
from .views import UserInfoGenericAPIView

urlpatterns = [
    path("userInfo", UserInfoGenericAPIView.as_view()),
]
