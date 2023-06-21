from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("v1/", include("apps.device.urls")),
    path("v1/", include("apps.user_info.urls")),
]
