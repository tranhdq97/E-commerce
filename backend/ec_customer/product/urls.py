from django.urls import path

from ec_base.common.constant.view_action import BaseViewAction
from ec_customer.product.views.viewset import ProductViewSet

urlpatterns = [
    path("list", ProductViewSet.as_view({"get": BaseViewAction.LIST})),
    path("<int:pk>/detail", ProductViewSet.as_view({"get": BaseViewAction.RETRIEVE})),
]
