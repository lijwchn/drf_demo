from rest_framework.response import Response
from rest_framework import status


class APIResponse(Response):
    def __init__(self, code=200, message="操作成功", success=True, data=None, status=status.HTTP_200_OK, **kwargs):
        """
        :param code: 错误码
        :param message: 返回信息
        :param data: 获取的数据
        :param status: HTTP状态码
        :param kwargs: 其他参数
        """
        response_data = {
            "code": code,
            "message": message,
            "success": success
        }
        if data:  # 将获取的数据data添加到字典
            response_data.update(data=data)
        if kwargs:  # 如果不为空，其他参数添加到字典
            response_data.update(kwargs)
        super().__init__(data=response_data, status=status)
