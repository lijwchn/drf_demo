from .models import Device
from .serializers import DeviceSerializer
from utils.api_response import APIResponse
from base_curd.page_setting import Pager
from base_curd.base_curd import BaseCURDView


class GetUpdateDeviceById(BaseCURDView):
    """
    get 根据对象id查询单个
    put 根据对象id更新
    """

    model = Device
    serializer_class = DeviceSerializer
    pagination_class = Pager

    def get(self, request, *args, **kwargs):
        # 根据id查询单个
        res = self.get_obj_by_id(request, *args, **kwargs)
        return APIResponse(data=res)

    def put(self, request, *args, **kwargs):
        # 根据对象id更新
        if self.update_obj_by_id(request, *args, **kwargs):
            return APIResponse(message="更新成功")


class GetCreateDeleteDevice(GetUpdateDeviceById):
    """
    get 查询列表
    post 新增
    delete 根据对象ids批量删除(和下面二选一)
    delete 根据对象ids批量软删除
    """

    def get(self, request, *args, **kwargs):
        # 分页查询列表
        res = self.get_obj_list_by_conditions_page(
            request, exact=False, *args, **kwargs
        )
        if self.pagination_class is not None:
            total_count = self.paginator.page.paginator.count
            total_page = self.paginator.page.paginator.num_pages
            return APIResponse(data=res, total_count=total_count, total_page=total_page)
        return APIResponse(data=res)

    def post(self, request, *args, **kwargs):
        res = self.create_obj(request, payload=request.data)
        if res:
            return APIResponse(message="创建成功")

    def delete(self, request, *args, **kwargs):
        if self.soft_delete_obj_by_ids(request, *args, **kwargs):
            return APIResponse(message="删除成功")

    # def delete(self, request, *args, **kwargs):
    #     if self.delete_obj_by_ids(request, *args, **kwargs):
    #         return APIResponse(message="删除成功")
