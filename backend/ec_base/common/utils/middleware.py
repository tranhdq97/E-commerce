import logging
import uuid
from threading import local

from django.conf import settings

logger = logging.getLogger(__name__)

USER_ATTR_NAME = getattr(settings, 'LOCAL_USER_ATTR_NAME', '_current_user')
REQ_UUID_ATTR_NAME = getattr(settings, 'LOCAL_REQ_UUID_ATTR_NAME', '_req_uuid')
_thread_locals = local()


def set_req_uuid(request_uuid):
    setattr(_thread_locals, REQ_UUID_ATTR_NAME, request_uuid)


def del_req_uuid():
    req_uuid = getattr(_thread_locals, REQ_UUID_ATTR_NAME, None)
    if req_uuid is not None:
        delattr(_thread_locals, REQ_UUID_ATTR_NAME)


def get_req_uuid():
    req_uuid = getattr(_thread_locals, REQ_UUID_ATTR_NAME, None)
    return req_uuid


class CorrelationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        req_uuid = uuid.uuid4()
        set_req_uuid(req_uuid)
        logger.info(f'START | path={request.path} | method={request.method}')
        response = self.get_response(request)
        logger.info(f'END   | path={request.path} | status={response.status_code} | user_logged={request.user}')
        del_req_uuid()
        return response


class RequestUuidFilter(logging.Filter):

    def filter(self, record):
        req_uuid = getattr(_thread_locals, REQ_UUID_ATTR_NAME, '')
        record.req_uuid = req_uuid
        return True
