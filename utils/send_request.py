import json
import cchardet
from retrying import retry
from utils.loguru_settings import logger
from requests import request, RequestException


@retry(stop_max_attempt_number=3, retry_on_result=lambda x: x is None, wait_fixed=2000)
def send_request(url, method=None, timeout=None, **kwargs):
    _maxTimeout = timeout if timeout else 5
    _method = method
    try:
        response = request(method=_method, url=url, **kwargs)
        encoding = cchardet.detect(response.content)['encoding']
        logger.info("请求地址{}".format(url))
        logger.info("接口入参{}".format(response.request.body))
        if response.status_code == 200:
            response_content = json.loads(response.content.decode(encoding))
            logger.info("接口出参{}".format(response_content))
            return response_content
        logger.error("状态码{}不能处理,接口url{}".format(response.status_code, url))
    except RequestException as e:
        logger.error("外部接口异常url:{},错误信息{}".format(url, e), exc_info=True)
