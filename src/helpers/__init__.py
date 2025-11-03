from loguru import logger

from .utils import get_soup_pw

__all__ = ["get_soup_pw"]


logger.add(
    "data/info.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} - {message}",
    level="INFO",
)
logger.info("the logger had started")
