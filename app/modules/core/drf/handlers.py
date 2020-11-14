from typing import Optional

import six
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import set_rollback

from modules.core.logging import custom_capture_message


def exception_handler(exc, context) -> Optional[Response]:
    if isinstance(exc, exceptions.ValidationError):
        return handle_validation_errors(exc, context)
    elif isinstance(exc, exceptions.APIException):
        return handle_api_errors(exc)
    elif isinstance(exc, Http404):
        return handle_not_found()
    elif isinstance(exc, PermissionDenied):
        return handle_permissions_denied()
    return None


def handle_api_errors(exc: exceptions.APIException) -> Response:
    headers = {}
    if getattr(exc, "auth_header", None):
        headers["WWW-Authenticate"] = exc.auth_header
    if getattr(exc, "wait", None):
        headers["Retry-After"] = "%d" % exc.wait

    data = exc.get_full_details()
    set_rollback()
    return Response(data, status=exc.status_code, headers=headers)


def handle_not_found() -> Response:
    data = {"message": six.text_type(_("Not found.")), "code": "not_found"}
    set_rollback()
    return Response(data, status=status.HTTP_404_NOT_FOUND)


def handle_permissions_denied() -> Response:
    data = {
        "message": six.text_type(_("Permission denied.")),
        "code": "permission_denied",
    }
    set_rollback()
    return Response(data, status=status.HTTP_403_FORBIDDEN)


def handle_validation_errors(
    exc: exceptions.ValidationError, context: dict
) -> Response:
    data = exc.get_full_details()
    message = getattr(exc, "message", repr(exc))
    custom_capture_message(
        msg=message,
        level="warning",
        extra={
            "status_code": status.HTTP_400_BAD_REQUEST,
            "request_body": context["request"].data,
            "response_body": data,
        },
    )
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
