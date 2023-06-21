from .models import UserInfo
from apps.basic.my_model_serializer import MySerializer
from rest_framework import serializers


class UserInfoSerializer(MySerializer):
    user_name = serializers.CharField()
    user_password = serializers.CharField()
    user_phone = serializers.CharField()

    class Meta:
        model = UserInfo
        fields = '__all__'
