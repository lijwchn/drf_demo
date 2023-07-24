from django.http import Http404
from rest_framework import mixins, generics
from utils.api_response import APIResponse
from rest_framework.generics import get_object_or_404, RetrieveAPIView
from typing import Any
from utils.loguru_settings import logger
import traceback


class BaseCURDView(RetrieveAPIView):
    model = None
    serializer_class = None
    pagination_class = None
    lookup_field = "id"

    def get_queryset(self):
        return self.model.objects.filter(is_delete=0)

    def get_obj_by_id(self, request, *args, **kwargs):
        # 根据id（pk）查询单个对象
        try:
            instance = self.get_queryset().get(**kwargs)
        except self.model.DoesNotExist:
            raise Http404("对象不存在")
        serializer = self.serializer_class(instance)
        return serializer.data

    def create_obj(self, request, creator: str, payload: Any):
        # 创建对象
        try:
            logger.info(
                f"input: create={self.model.__name__}, payload={payload}")
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            obj = self.model.objects.create(creator=creator, **payload)
            logger.info(f"create {self.model.__name__} success, id: {obj.id}")
            return True
        except Exception as e:
            logger.warning(traceback.format_exc())
            raise e

    def get_obj_list_by_conditions(
            self, request, exact: bool, *args, **kwargs):
        # 使用条件查询对象列表
        filter_conditions = request.query_params.dict()
        filter_conditions.update({"is_delete": 0})  # 添加过滤条件
        if exact:
            obj = self.model.objects.filter(**filter_conditions)
        else:
            obj = self.model.objects.filter(
                **{f'{key}__contains': value for key, value in filter_conditions.items()})
        ser = self.serializer_class(obj, many=True)
        return ser.data

    def delete_obj_by_ids(self):
        ...

    def soft_delete_obj_by_ids(self):
        ...

    def update_obj_by_id(self):
        ...
