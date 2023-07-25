from django.http import Http404
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from typing import Any
from utils.loguru_settings import logger
from utils.custom_exception import BaseCustomException
import traceback
from django.utils import timezone


class BaseCURDView(RetrieveAPIView, GenericAPIView):
    model = None
    serializer_class = None
    pagination_class = None
    lookup_field = "id"

    def get_queryset(self):
        queryset = self.model.objects.filter(is_delete=0)
        return queryset

    def get_obj_by_id(self, request, *args, **kwargs):
        # 根据id（pk）查询单个对象
        try:
            instance = self.get_queryset().get(**kwargs)
        except self.model.DoesNotExist:
            raise Http404("对象不存在")
        serializer = self.serializer_class(instance)
        return serializer.data

    def get_obj_list_by_conditions_page(
            self, request, exact: bool, *args, **kwargs):
        """
        使用条件查询对象列表
        :param request:
        :param exact: 是否开启精确查询 True False
        :param args:
        :param kwargs:
        :return:
        """
        filter_conditions = request.query_params.dict()
        # 删除page page_size 这两个过滤条件
        keys_to_remove = ["page", "page_size"]
        for key in keys_to_remove:
            filter_conditions.pop(key, None)
        if exact:
            obj = self.get_queryset().filter(**filter_conditions)
        else:
            obj = self.get_queryset().filter(
                **{f'{key}__contains': value for key, value in filter_conditions.items()})
        if self.pagination_class is not None:
            logger.info("需要分页查询")
            obj = self.paginate_queryset(obj.order_by("id"))
            ser = self.serializer_class(obj, many=True)
            return ser.data
        else:
            ser = self.serializer_class(obj, many=True)
            return ser.data

    def create_obj(self, request, payload: Any, creator: str = "sys"):
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
            logger.error(traceback.format_exc())
            raise e

    def delete_obj_by_ids(self, request, *args, **kwargs):
        try:
            # 获取传入的ids数据
            ids_data = request.data.get("ids", [])
            if not isinstance(ids_data, list):
                raise BaseCustomException(detail="ids必须是一个列表")
            queryset = self.get_queryset().filter(id__in=ids_data)
            queryset.delete()
            return True
        except Exception as e:
            logger.error(traceback.format_exc())
            raise e

    def soft_delete_obj_by_ids(self, request, *args, **kwargs):
        try:
            # 获取传入的ids数据
            ids_data = request.data.get("ids", [])
            if not isinstance(ids_data, list):
                raise BaseCustomException(detail="ids必须是一个列表")
            if len(ids_data) == 0:
                raise BaseCustomException(detail="需要删除的数据为空")
            queryset = self.get_queryset().filter(id__in=ids_data)
            queryset.update(is_delete=1, update_time=timezone.now())
            return True
        except Exception as e:
            logger.error(traceback.format_exc())
            raise e

    def update_obj_by_id(self, request, *args, **kwargs):
        try:
            instance = self.get_object()  # 获取要更新的对象
            data = request.data  # 获取请求的数据
            serializer = self.serializer_class(
                instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return True
        except Exception as e:
            logger.error(traceback.format_exc())
            raise e
