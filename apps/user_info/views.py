from django.utils import timezone
from rest_framework.generics import GenericAPIView
from .models import UserInfo
from .serializers import UserInfoSerializer
from utils.api_response import APIResponse
from utils.custom_exception import BaseCustomException


class UserInfoGenericAPIView(GenericAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def get(self, request):
        user_queryset = self.get_queryset().filter(is_delete=0)
        user_serializer = self.get_serializer(user_queryset, many=True)
        return APIResponse(data=user_serializer.data)

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, dict):
            # 调用模型序列化器，反序列化
            user_serializer = self.get_serializer(data=request.data)
            # 校验数据, raise_exception 数据不合格之后抛异常
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()
            return APIResponse(data="success")
        else:
            raise BaseCustomException("数据格式错误")

    def put(self, request, *args, **kwargs):
        pk = request.data.get("id")
        if pk is not None and self.queryset.filter(id=pk).exists():
            user = self.get_queryset().filter(pk=pk).first()
            serializer = self.get_serializer(instance=user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return APIResponse(data="success")
        else:
            raise BaseCustomException("根据id找不到需要修改的数据")

    def delete(self, request, *args, **kwargs):
        del_list = request.data.get("ids")
        num = (
            self.get_queryset()
            .filter(pk__in=del_list, is_delete=0)
            .update(is_delete=1, update_time=timezone.now())
        )
        if num:
            return APIResponse(message="删除了{}条数据".format(num))
        raise BaseCustomException("没有删除数据,删除的数据可能不存在,或者已经被删除")
