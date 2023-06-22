from .models import UserInfo
from apps.basic.my_serializer import MySerializer
from rest_framework import serializers


class UserInfoSerializer(MySerializer):
    user_name = serializers.CharField()
    user_password = serializers.CharField()
    user_phone = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        return UserInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.user_name = validated_data.get("user_name")
        # instance.user_password = validated_data.get("user_password")
        # instance.user_phone = validated_data.get("user_phone")
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
