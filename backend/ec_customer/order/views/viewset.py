from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ec_base.auth.permissions.permission import IsVerified
from ec_base.common.constant.view_action import BaseViewAction, OrderViewAction
from ec_base.common.custom.pagination import CustomPagination
from ec_base.common.utils.exceptions import PermissionDenied
from ec_base.order.models import Order
from ec_customer.order.serializers.order import OrderRetrieveSlz, OrderListSlz, OrderCreateSlz
from ec_customer.order.services.order import OrderSvc


class OrderViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    serializer_class = OrderListSlz
    queryset = Order.objects.filter()

    def get_serializer_class(self):
        slz_switcher = {
            BaseViewAction.LIST: OrderListSlz,
            BaseViewAction.RETRIEVE: OrderRetrieveSlz,
            BaseViewAction.CREATE: OrderCreateSlz,
        }
        return slz_switcher.get(self.action, OrderListSlz)

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.LIST: (IsVerified,),
            BaseViewAction.RETRIEVE: (IsVerified,),
            BaseViewAction.CREATE: (IsVerified,),
            OrderViewAction.CANCEL: (IsVerified,),
        }
        self.permission_classes = perm_switcher.get(self.action)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        svc = OrderSvc()
        return Response(svc.create(data=request.data, serializer=self.get_serializer_class()).data)

    def cancel(self, request, *args, **kwargs):
        svc = OrderSvc()
        svc.cancel(order=self.get_object())
        return Response(status=status.HTTP_204_NO_CONTENT)
