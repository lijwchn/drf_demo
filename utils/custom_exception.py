from rest_framework.exceptions import APIException
from rest_framework import status


class BaseCustomException(APIException):
    """
    通用异常类
    """

    default_detail = "系统内部异常"
    status_code = status.HTTP_200_OK

    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)
        detail = self.default_detail
        code = self.default_code


class NotAuthenticated(BaseCustomException):
    default_detail = "未通过身份验证"
    status_code = status.HTTP_401_UNAUTHORIZED


class ParseError(APIException):
    default_detail = "格式错误"
    status_code = status.HTTP_400_BAD_REQUEST


class PermissionDenied(APIException):
    default_detail = "无权限执行操作"
    status_code = status.HTTP_403_FORBIDDEN


class NotFound(APIException):
    default_detail = "数据不存在"
    status_code = status.HTTP_404_NOT_FOUND
