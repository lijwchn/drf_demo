import time
from utils.loguru_settings import logger
from django.utils.deprecation import MiddlewareMixin


class LoggingMiddleware(MiddlewareMixin):
    """
    全局日志中间件
    """

    def process_request(self, request):
        # 存放请求过来时的时间
        request.init_time = time.time()
        request.body.decode("utf-8")
        return None

    def process_response(self, request, response):
        time_cost = time.time() - request.init_time  # 耗时
        path = request.path  # 请求路径
        method = request.method  # 请求方式
        # 请求参数
        if method == "GET":
            query = request.GET
            parm = query.urlencode()
        else:
            parm = request.body.decode("utf-8")
        status_code = response.status_code  # 响应状态码
        response_content = response.content.decode("utf-8")  # 响应参数
        message = (
            f"\nurl:{path}"
            f"\nmethod:{method}"
            f"\nparm:{parm},"
            f"\ntime_cost:{round(time_cost * 1000, 3)}ms"
            f"\nstatus_code:{status_code}"
            f"\nresponse_content:{response_content}"
        )
        logger.info(message)
        return response
