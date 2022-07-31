import logging
import uuid
from threading import local

from django.conf import settings

logger = logging.getLogger(__name__)

USER_ATTR_NAME = getattr(settings, 'LOCAL_USER_ATTR_NAME', '_current_user')
REQ_UUID_ATTR_NAME = getattr(settings, 'LOCAL_REQ_UUID_ATTR_NAME', '_req_uuid')
_thread_locals = local()


def set_current_user(user_func):
    setattr(_thread_locals, USER_ATTR_NAME, user_func.__get__(user_func, local))


def del_current_user():
    delattr(_thread_locals, USER_ATTR_NAME)


def set_req_uuid(request_uuid):
    setattr(_thread_locals, REQ_UUID_ATTR_NAME, request_uuid)


def del_req_uuid():
    req_uuid = getattr(_thread_locals, REQ_UUID_ATTR_NAME, None)
    if req_uuid is not None:
        delattr(_thread_locals, REQ_UUID_ATTR_NAME)


def get_current_user():
    current_user = getattr(_thread_locals, USER_ATTR_NAME, None)
    if callable(current_user):
        return current_user()

    return current_user


def get_req_uuid():
    req_uuid = getattr(_thread_locals, REQ_UUID_ATTR_NAME, None)
    return req_uuid


class CorrelationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        req_uuid = uuid.uuid4()
        set_req_uuid(req_uuid)
        set_current_user(lambda: getattr(request, 'user', None))

        logger.info(f'START: "{request.path} {request.method}"')

        response = self.get_response(request)
        current_user = request.user
        provider = getattr(current_user, 'provider', '')

        logger.info(f'END "{request.path} {request.status_code}" user_logged={current_user}, provider={provider}')

        del_current_user()
        del_req_uuid()
        return response


class RequestUuidFilter(logging.Filter):

    def filter(self, record):
        req_uuid = getattr(_thread_locals, REQ_UUID_ATTR_NAME, '')
        record.req_uuid = req_uuid
        return True
