from loguru import logger

# 添加定义好的普通日志文件,并设置格式和级别等信息
# rotation表示
logger.add(
    "logs/biz.log",
    format="{time} {level} {message}",
    level="INFO",
    encoding="utf-8",
)
# 添加定义好的错误日志文件,并设置格式和级别等信息
logger.add(
    "logs/error.log",
    format="{time} {level} {message}",
    level="ERROR",
    encoding="utf-8",
)
