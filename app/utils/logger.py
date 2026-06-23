import logging
import time
from functools import wraps

# 配置日志格式
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # 输出到控制台
        logging.FileHandler("logs/app.log")  # 输出到文件
    ]
)

logger = logging.getLogger("mini-chat-api")

def log_time(func):
    """装饰器：记录函数执行耗时"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.info(f"{func.__name__} 执行耗时: {elapsed:.2f}s")
        return result
    return wrapper