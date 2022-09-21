import logging

from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import exception_handler, set_rollback

logger = logging.getLogger(__name__)


def server_error(request, *args, **kwargs):
    """Generic 500 error handler."""
    data = {"status_code": "error", "message": _("Internal Service error"), "details": []}
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and isinstance(exc, exceptions.APIException):
        headers = {}

        if getattr(exc, "auth_header", None):
            headers["WWW-Authenticate"] = exc.auth_header
        if getattr(exc, "wait", None):
            headers["Retry-After"] = "%d" % exc.wait

        data = {
            "status_code": exc.default_code,
            "message": exc.default_detail if isinstance(exc.detail, (list, dict)) else exc.detail,
            "detail": exc.detail,
        }
        set_rollback()
        logger.warning(f"API bad request {exc}")
        return Response(data, status=exc.status_code, headers=headers)

    return response
