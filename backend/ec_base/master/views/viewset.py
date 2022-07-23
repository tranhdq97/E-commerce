from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..filters.base_master import BaseMasterListQueryFields
from ..serializers.base_master import BaseMasterCreateSerializer, BaseMasterListSerializer, BaseMasterListReqParams
from ..services.base_master import BaseMasterService
from ...common.constant.db_fields import MasterFields
from ...common.constant.db_table import DBTable


class MasterViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    pagination_class = None
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    serializer_class = BaseMasterListSerializer
    search_fields = BaseMasterListQueryFields.SEARCH_FIELDS
    ordering_fields = BaseMasterListQueryFields.ORDER_FIELDS
    ordering = BaseMasterListQueryFields.ORDER_DEFAULT_FIELD

    def destroy(self, request, *args, **kwargs):
        master_name = kwargs.pop('_'.join([DBTable.MASTER, MasterFields.NAME]))
        pk = kwargs.pop(MasterFields.ID)
        service = BaseMasterService(master_name)
        service.delete(pk)
        return Response(status=200)

    @extend_schema(parameters=[BaseMasterListReqParams])
    def list(self, request, **kwargs):
        master_name = kwargs.pop('_'.join([DBTable.MASTER, MasterFields.NAME]))
        service = BaseMasterService(master_name)
        queryset = service.list(parent_id=request.query_params.get(MasterFields.PARENT_ID))
        queryset = self.filter_queryset(queryset)
        queryset = queryset.filter(is_deleted=False, **kwargs)
        serializer = service.get_master_list_serializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(parameters=[BaseMasterCreateSerializer])
    def create(self, request, **kwargs):
        master_name = kwargs.pop('_'.join([DBTable.MASTER, MasterFields.NAME]))
        service = BaseMasterService(master_name)
        serializer = service.create(request.query_params)
        return Response(serializer.data)
