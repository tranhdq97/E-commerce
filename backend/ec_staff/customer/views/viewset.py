from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from ec_base.auth.permissions.permission import IsApproved
from ec_base.common.constant import message
from ec_base.common.constant.view_action import BaseViewAction
from ec_base.common.custom.pagination import CustomPagination
from ec_base.common.utils.exceptions import PermissionDenied, APIErr
from ec_base.customer.models import Customer
from ec_staff.customer.filters.customer import CustomerListQueryFields
from ec_staff.customer.serializers.customer import CustomerListSlz, CustomerRetrieveSlz


class CustomerViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    serializer_class = CustomerListSlz
    queryset = Customer.objects.all()
    search_fields = CustomerListQueryFields.SEARCH_FIELDS
    ordering_fields = CustomerListQueryFields.ORDER_FIELDS
    ordering = CustomerListQueryFields.ORDER_DEFAULT_FIELD

    def get_serializer_class(self):
        slz_switcher = {
            BaseViewAction.LIST: CustomerListSlz,
            BaseViewAction.RETRIEVE: CustomerRetrieveSlz,
        }
        slz = slz_switcher.get(self.action)
        if slz is None:
            raise APIErr(message.NO_SERIALIZER_MATCHED)

        return slz

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.LIST: (IsApproved,),
            BaseViewAction.RETRIEVE: (IsApproved,),
        }
        self.permission_classes = perm_switcher.get(self.action)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()
