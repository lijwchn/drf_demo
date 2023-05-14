import traceback
from rest_framework import status
from rest_framework.views import exception_handler
from .api_response import APIResponse
from utils.loguru_settings import logger
from rest_framework.exceptions import ValidationError


def comm_exception_handler(exc=None, context=None):
    logger.error(traceback.format_exc())
    response = exception_handler(exc, context)
    # 判断是否有值，有值代表是DRF的异常，没值就是其它异常
    if response is not None:
        detail = response.data.get("detail") or exc.detail
        if isinstance(exc, ValidationError):
            first_key, first_value = next(iter(exc.detail.items()))
            detail = f"{first_key}{first_value[0]}"
        # status_code = response.status_code
        return APIResponse(code=500, message=detail, status=status.HTTP_200_OK, success=False)
    return APIResponse(code=500, message="系统异常", status=status.HTTP_200_OK, success=False)
