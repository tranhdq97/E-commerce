from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from ec_base.auth.permissions.permission import IsSuperStaff, IsManager, IsApproved
from ec_base.common.constant.view_action import BaseViewAction
from ec_base.common.custom.pagination import CustomPagination
from ec_base.common.serializer.custom_mixins import CustomDestroyMixin
from ec_base.common.utils.exceptions import PermissionDenied
from ec_base.discount.models import Discount
from ec_staff.discount.filters.discount import DiscountListQueryFields
from ec_staff.discount.serializers.discount import DiscountListSlz, DiscountRetrieveSlz, DiscountCreateSlz, \
    DiscountUpdateSlz


class DiscountViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin, CustomDestroyMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    serializer_class = DiscountListSlz
    queryset = Discount.objects.filter(is_deleted=False)
    search_fields = DiscountListQueryFields.SEARCH_FIELDS
    ordering_fields = DiscountListQueryFields.ORDER_FIELDS
    ordering = DiscountListQueryFields.ORDER_DEFAULT_FIELD

    def get_serializer_class(self):
        slz_switcher = {
            BaseViewAction.LIST: DiscountListSlz,
            BaseViewAction.RETRIEVE: DiscountRetrieveSlz,
            BaseViewAction.CREATE: DiscountCreateSlz,
            BaseViewAction.UPDATE: DiscountUpdateSlz,
        }
        return slz_switcher.get(self.action, DiscountListSlz)

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.LIST: (AllowAny,),
            BaseViewAction.RETRIEVE: (IsApproved,),
            BaseViewAction.CREATE: (IsSuperStaff | IsManager,),
            BaseViewAction.UPDATE: (IsSuperStaff | IsManager,),
            BaseViewAction.DESTROY: (IsSuperStaff | IsManager,),
        }
        self.permission_classes = perm_switcher.get(self.action)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()
