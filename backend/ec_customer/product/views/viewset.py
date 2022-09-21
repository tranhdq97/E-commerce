from django.db.models import Avg
from django.db.models.functions import Round
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from ec_base.common.constant.view_action import BaseViewAction
from ec_base.common.custom.pagination import CustomPagination
from ec_base.common.utils.exceptions import PermissionDenied
from ec_base.product.models import Product
from ec_customer.product.filters.product import ProductListQueryFields
from ec_customer.product.serializers.product import ProductListSlz, ProductRetrieveSlz


class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    serializer_class = ProductListSlz
    queryset = Product.objects.all()
    search_fields = ProductListQueryFields.SEARCH_FIELDS
    ordering_fields = ProductListQueryFields.ORDER_FIELDS
    ordering = ProductListQueryFields.ORDER_DEFAULT_FIELD
    filterset_fields = ProductListQueryFields.FILTERSET_FIELDS

    def get_queryset(self):
        queryset = Product.objects.all().prefetch_related("rating").annotate(num_stars=Round(Avg("rating__num_stars")))
        return queryset

    def get_serializer_class(self):
        slz_switcher = {
            BaseViewAction.LIST: ProductListSlz,
            BaseViewAction.RETRIEVE: ProductRetrieveSlz,
        }
        slz = slz_switcher.get(self.action, ProductListSlz)
        return slz

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.LIST: (AllowAny,),
            BaseViewAction.RETRIEVE: (AllowAny,),
        }
        self.permission_classes = perm_switcher.get(self.action)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()
