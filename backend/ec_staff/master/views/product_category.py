from django_filters.rest_framework.backends import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ec_base.auth.permissions.permission import IsStaff
from ec_base.common.constant.constant import DateTimeFormat
from ec_base.common.constant.db_fields import CommonFields
from ec_base.common.constant.master import MasterFilterByID
from ec_base.common.constant.view_action import ProductCategoryViewAction
from ec_base.common.custom.pagination import CustomPagination
from ec_base.common.utils.exceptions import PermissionDenied
from ec_base.master.models import MasterProductCategory
from ec_staff.master.serializers.product_category import SaleQuantityOverviewListSlz, SaleAmountOverviewListSlz, \
    OverviewReqParams
from ec_staff.master.services.product_category import ProductCategorySvc


class ProductCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = (IsStaff,)
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    serializer_class = None
    queryset = MasterProductCategory.objects.filter(is_deleted=False)

    def get_serializer_class(self):
        slz_switcher = {
            ProductCategoryViewAction.GET_SALE_QUANTITY_OVERVIEW: SaleQuantityOverviewListSlz,
            ProductCategoryViewAction.GET_SALE_AMOUNT_OVERVIEW: SaleAmountOverviewListSlz,
        }
        slz = slz_switcher.get(self.action, None)
        return slz

    def get_permissions(self):
        perm_switcher = {
            ProductCategoryViewAction.GET_SALE_QUANTITY_OVERVIEW: (IsStaff,),
            ProductCategoryViewAction.GET_SALE_AMOUNT_OVERVIEW: (IsStaff,),
        }
        self.permission_classes = perm_switcher.get(self.action)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()

    @extend_schema(parameters=[OverviewReqParams])
    def get_sale_quantity_overview(self, request, *args, **kwargs):
        filter_by_id = int(request.query_params.get(CommonFields.FILTER_BY_ID, MasterFilterByID.TODAY))
        svc = ProductCategorySvc()
        data = svc.get_sale_quantity_overview(
            filter_by_id=filter_by_id,
            slz_class=self.get_serializer_class(),
            timezone_offset=request.headers.get(DateTimeFormat.TIMEZONE_OFFSET),
        )
        return Response(data)

    @extend_schema(parameters=[OverviewReqParams])
    def get_sale_amount_overview(self, request, *args, **kwargs):
        filter_by_id = int(request.query_params.get(CommonFields.FILTER_BY_ID, MasterFilterByID.TODAY))
        svc = ProductCategorySvc()
        data = svc.get_sale_amount_overview(
            filter_by_id=filter_by_id,
            slz_class=self.get_serializer_class(),
            timezone_offset=request.headers.get(DateTimeFormat.TIMEZONE_OFFSET),
        )
        return Response(data)
