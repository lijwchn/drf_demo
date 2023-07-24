from rest_framework import mixins, generics
from utils.api_response import APIResponse
from rest_framework.generics import get_object_or_404
from typing import Any
from utils.loguru_settings import logger
import traceback


class BaseCURDView:
    model = None
    serializer_class = None
    pagination_class = None

    def get_queryset(self):
        return self.model.objects.all()

    def get_obj_by_pk(self, pk: int):
        # 根据id（pk）查询单个对象
        instance = get_object_or_404(queryset=self.get_queryset(), id=pk)
        return self.serializer_class(instance)

    def create_obj(self, creator: str, payload: Any):
        # 创建对象
        try:
            logger.info(
                f"input: create={self.model.__name__}, payload={payload}")
            obj = self.model.objects.create(creator=creator, **payload)
        except Exception as e:
            logger.warning(traceback.format_exc())
            raise e
        logger.info(f"create {self.model.__name__} success, id: {obj.id}")

    def get_obj_list_by_conditions(
            self, request, exact: bool, *args, **kwargs):
        # 使用条件查询对象列表
        filter_conditions = request.query_params.dict()
        if exact:
            obj = self.model.objects.filter(**filter_conditions)
        else:
            obj = self.model.objects.filter(
                **{f'{key}__contains': value for key, value in filter_conditions.items()})
        ser = self.serializer_class(obj, many=True)
        return ser.data

