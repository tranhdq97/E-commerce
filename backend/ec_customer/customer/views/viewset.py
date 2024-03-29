from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ec_base.auth.permissions.permission import IsCustomer
from ec_base.common.constant import message
from ec_base.common.constant.view_action import BaseViewAction
from ec_base.common.utils.exceptions import PermissionDenied, APIErr
from ec_base.customer.models import Customer
from ec_customer.customer.serializers.customer import CustomerUpdateSlz, CustomerCreateSlz, CustomerRetrieveSlz
from ec_customer.customer.services.customer import CustomerSvc


class CustomerViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CustomerCreateSlz
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        slz_switcher = {
            BaseViewAction.CREATE: CustomerCreateSlz,
            BaseViewAction.UPDATE: CustomerUpdateSlz,
            BaseViewAction.RETRIEVE: CustomerRetrieveSlz,
        }
        slz = slz_switcher.get(self.action)
        if slz is None:
            raise APIErr(message.NO_SERIALIZER_MATCHED)

        return slz

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.CREATE: (AllowAny,),
            BaseViewAction.UPDATE: (IsCustomer,),
            BaseViewAction.RETRIEVE: (IsCustomer,),
        }
        self.permission_classes = perm_switcher.get(self.action)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        svc = CustomerSvc()
        slz = svc.update_customer(pk=request.user.id, data=request.data)
        return Response(slz.data)
