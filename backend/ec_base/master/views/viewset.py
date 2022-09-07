from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ec_base.auth.permissions.permission import IsManager, IsSuperStaff
from ec_base.common.constant.db_fields import CommonFields, MasterFields
from ec_base.common.constant.db_table import DBTable
from ec_base.common.constant.service import Master
from ec_base.common.constant.view_action import BaseViewAction
from ec_base.common.utils.exceptions import PermissionDenied
from ec_base.master.filters.base_master import BaseMasterListQueryFields
from ec_base.master.serializers.base_master import BaseMasterListReqParams, BaseMasterListSlz, BaseMasterCreateSlz
from ec_base.master.services.base_master import MasterBaseService


class MasterViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    pagination_class = None
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = BaseMasterListQueryFields.SEARCH_FIELDS
    ordering_fields = BaseMasterListQueryFields.ORDER_FIELDS
    ordering = BaseMasterListQueryFields.ORDER_DEFAULT_FIELD

    def get_serializer_class(self):
        slz_switcher = {
            BaseViewAction.CREATE: BaseMasterCreateSlz,
            BaseViewAction.LIST: BaseMasterListSlz,
        }
        return slz_switcher.get(self.action, BaseMasterListSlz)

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.LIST: (AllowAny,),
            BaseViewAction.DESTROY: (IsSuperStaff | IsManager,),
            BaseViewAction.CREATE: (IsSuperStaff | IsManager,)
        }
        self.permission_classes = perm_switcher.get(self.action)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()

    @extend_schema(description=f'Choices: {" | ".join(Master.list(allowed_to_create=False))}')
    def destroy(self, request, *args, **kwargs):
        master_name = kwargs.pop('_'.join([DBTable.MASTER, MasterFields.NAME]))
        pk = kwargs.pop(CommonFields.ID)
        service = MasterBaseService(master_name)
        service.delete(pk)
        return Response(status=200)

    @extend_schema(parameters=[BaseMasterListReqParams],
                   description=f'Choices: {" | ".join(Master.list(allowed_to_create=False))}')
    def list(self, request, **kwargs):
        master_name = kwargs.pop('_'.join([DBTable.MASTER, MasterFields.NAME]))
        service = MasterBaseService(master_name)
        queryset = service.list(parent_id=request.query_params.get(MasterFields.PARENT_ID))
        queryset = self.filter_queryset(queryset).filter(is_deleted=False, **kwargs)
        serializer = service.get_master_list_serializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(description=f'Choices: {" | ".join(Master.list(allowed_to_create=True))}')
    def create(self, request, **kwargs):
        master_name = kwargs.pop('_'.join([DBTable.MASTER, MasterFields.NAME]))
        service = MasterBaseService(master_name)
        serializer = service.create(request.data)
        return Response(serializer.data)
