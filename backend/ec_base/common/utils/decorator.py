import logging

logger = logging.getLogger(__name__)


def log(func):
    func_name = func.__name__

    def inner(*args, **kwargs):
        logger.info(f'START | {func_name}')
        logger.debug(f'START | {func_name} | args: {locals().get("args")} | kwargs: {locals().get("kwargs")}')
        result = func(*args, **kwargs)
        logger.info(f'END   | {func_name}')
        logger.debug(f'END   | {func_name}')
        return result

    return inner
