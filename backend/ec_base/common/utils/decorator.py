import logging

logger = logging.getLogger(__name__)


def log(func):
    func_name = func.__name__

    def inner(*args, **kwargs):
        logger.info(f'Start | {func_name}')
        logger.debug(f'Start | {func_name} | args: {locals().get("args")} | kwargs: {locals().get("kwargs")}')
        result = func(*args, **kwargs)
        logger.info(f'End   | {func_name}')
        logger.debug(f'End   | {func_name}')
        return result

    return inner
