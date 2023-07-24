from django.utils import timezone
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Device
from .serializers import DeviceSerializer
from utils.api_response import APIResponse
from base_curd.page_setting import Pager
from utils.custom_exception import BaseCustomException
from rest_framework.generics import get_object_or_404
from base_curd.base_curd import BaseCURDView


# class DeviceGenericAPIView(GenericAPIView):
#     queryset = Device.objects.all()
#     serializer_class = DeviceSerializer
#     pagination_class = Pager
#
#     def get(self, request, exact: bool = False, *args, **kwargs):
#
#         filter_conditions = self.request.query_params.dict()
#         if exact:
#             obj = self.queryset.filter(**filter_conditions)
#         else:
#             obj = self.queryset.filter(
#                 **{f'{key}__contains': value for key, value in filter_conditions.items()})
#
#         page = self.paginate_queryset(obj)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(obj, many=True)
#         return Response(serializer.data)

# class DeviceGenericAPIView(BaseCURDView, GenericAPIView):
#     model = Device
#     serializer_class = DeviceSerializer
#     pagination_class = None
#
#     def get(self, request, *args, **kwargs):
#         res = self.get_obj_list_by_conditions(
#             request, exact=False, *args, **kwargs)
#         return APIResponse(data=res)

class DeviceGenericAPIView(BaseCURDView, GenericAPIView):
    model = Device
    serializer_class = DeviceSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        res = self.get_obj_list_by_conditions(
            request, exact=False, *args, **kwargs)
        return APIResponse(data=res)