from rest_framework.views import APIView
from .models import Device
from .serializers import DeviceSerializer
from utils.api_response import APIResponse
from base_curd.page_setting import Pager
from utils.custom_exception import BaseCustomException
from rest_framework.generics import get_object_or_404
from base_curd.base_curd import BaseCURDView


class DeviceGenericAPIView(BaseCURDView, APIView):
    model = Device
    serializer_class = DeviceSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        # 查询列表
        res = self.get_obj_list_by_conditions(
            request, exact=False, *args, **kwargs)
        return APIResponse(data=res)

    # def get(self, request, *args, **kwargs):
    #     # 根据id查询单个
    #     res = self.get_obj_by_id(request, *args, **kwargs)
    #     return APIResponse(data=res)

    def post(self, request, *args, **kwargs):
        res = self.create_obj(request, creator="sys", payload=request.data)
        if res:
            return APIResponse(message="创建成功")
