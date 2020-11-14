from django import http


def page_not_found(*args, **kwargs):
    return http.JsonResponse({"code": "not_found", "message": "Not found."}, status=404)


def server_error(*args, **kwargs):
    return http.JsonResponse(
        {"code": "server_error", "message": "Server error."}, status=500
    )


def bad_request(*args, **kwargs):
    return http.JsonResponse(
        {"code": "bad_request", "message": "Bad Request."}, status=400
    )


def permission_denied(*args, **kwargs):
    return http.JsonResponse({"code": "forbidden", "message": "Forbidden."}, status=403)
