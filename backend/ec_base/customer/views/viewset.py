from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..filters.customer import CustomerListQueryFields
from ..models import Customer
from ..serializers.customer import CustomerListSlz, CustomerCreateSlz, CustomerUpdateSlz, CustomerRetrieveSlz
from ..services.customer import CustomerSvc
from ...auth.permissions.permission import IsApproved
from ...common.constant import message
from ...common.constant.view_action import BaseViewAction
from ...common.custom.exceptions import PermissionDenied, APIErr
from ...common.custom.pagination import CustomPagination


class CustomerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin, GenericViewSet):
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
            BaseViewAction.CREATE: CustomerCreateSlz,
            BaseViewAction.UPDATE: CustomerUpdateSlz
        }
        slz = slz_switcher.get(self.action)
        if slz is None:
            raise APIErr(message.NO_SERIALIZER_MATCHED)

        return slz

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.LIST: (IsApproved,),
            BaseViewAction.RETRIEVE: (IsApproved,),
            BaseViewAction.CREATE: (IsApproved,),
            BaseViewAction.UPDATE: (IsApproved,),
        }
        self.permission_classes = perm_switcher.get(self.action)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        svc = CustomerSvc()
        slz = svc.update_customer(pk=kwargs.pop('pk'), data=request.data)
        return Response(slz.data)
