from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def api_health_check(*args, **kwargs):
    return Response({"status": "ok"}, status=status.HTTP_200_OK)
