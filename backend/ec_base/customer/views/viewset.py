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
from ...common.constant.view_action import BaseViewAction
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
        slz = slz_switcher.get(self.action, None)
        if slz is None:
            raise ValueError('There is no serializer matched with this action')

        return slz

    def update(self, request, *args, **kwargs):
        svc = CustomerSvc()
        slz = svc.update_customer(pk=kwargs.pop('pk'), data=request.data)
        return Response(slz.data)