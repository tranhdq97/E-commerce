from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from ..permissions.permission import IsStaff
from ..serializers.auth import ChangePasswordSlz
from ..services.auth import AuthSvc


@extend_schema(
    methods=['PUT'],
    tags=['auth'],
    request=ChangePasswordSlz,
    responses={200: {}},
    description='Change password'
)
@api_view(['PUT'])
@permission_classes([IsStaff])
def change_password(request):
    service = AuthSvc()
    data = service.change_password(request.user, request.data)
    return Response(data=data)


@extend_schema(
    methods=['GET'],
    tags=['auth'],
    description='Get me',
    request=None,
    responses={200: {}}
)
@api_view(["GET"])
@permission_classes([IsStaff])
def get_me(request):
    service = AuthSvc()
    data = service.get_me(request.user)
    return Response(data=data)
