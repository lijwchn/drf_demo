from django.utils import timezone
from rest_framework.generics import GenericAPIView
from .models import Device
from .serializers import DeviceSerializer
from utils.api_response import APIResponse
from base_curd.page_setting import Pager
from utils.custom_exception import BaseCustomException


class DeviceGenericAPIView(GenericAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    pagination_class = Pager

    def get(self, request):
        code = request.query_params.get("code") or ""
        name = request.query_params.get("name") or ""
        item_queryset = self.get_queryset().filter(
            is_delete=0, code__contains=code, name__contains=name)
        # logger.info(item_queryset.query)
        item_page = self.paginate_queryset(item_queryset)
        item_serializer = self.get_serializer(item_page, many=True)
        # item_serializer = self.get_serializer(item_queryset, many=True)
        total_count = self.paginator.page.paginator.count
        total_page = self.paginator.page.paginator.num_pages
        if len(item_serializer.data) == 0:
            return APIResponse(data="无数据")
        return APIResponse(data=item_serializer.data, totalCount=total_count,
                           totalPage=total_page)
        # return APIResponse(data=item_serializer.data)

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, dict):
            serializer = self.get_serializer(data=request.data)
            # 校验数据, raise_exception 数据不合格之后抛异常
            serializer.is_valid(raise_exception=True)
            # 保存数据
            serializer.save()
            return APIResponse(data="success")
        else:
            raise BaseCustomException("数据格式错误")

    def put(self, request, *args, **kwargs):
        pk = request.data.get("id")
        if self.queryset.filter(id=pk).exists():
            device = self.get_queryset().filter(pk=pk).first()
            serializer = self.get_serializer(
                instance=device, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return APIResponse(data="success")
        else:
            raise BaseCustomException("根据id找不到需要修改的数据")

    def delete(self, request, *args, **kwargs):
        del_list = request.data.get("ids")
        num = self.get_queryset().filter(
            pk__in=del_list, is_delete=0).update(
            is_delete=1, update_time=timezone.now())
        if num:
            return APIResponse(message="删除了{}条数据".format(num))
        raise BaseCustomException("没有删除数据,删除的数据可能不存在,或者已经被删除")
