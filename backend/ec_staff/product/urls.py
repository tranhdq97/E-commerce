from django.urls import path

from ec_base.common.constant.view_action import BaseViewAction, ProductViewAction
from ec_staff.product.views.viewset import ProductViewSet

urlpatterns = [
    path("create", ProductViewSet.as_view({"post": BaseViewAction.CREATE})),
    path("list", ProductViewSet.as_view({"get": BaseViewAction.LIST})),
    path("<int:pk>/detail", ProductViewSet.as_view({"get": BaseViewAction.RETRIEVE})),
    path("<int:pk>/delete", ProductViewSet.as_view({"delete": BaseViewAction.DESTROY})),
    path("<int:pk>/update", ProductViewSet.as_view({"put": BaseViewAction.UPDATE})),
    path("<int:pk>/update-quantity", ProductViewSet.as_view({"put": ProductViewAction.UPDATE_QUANTITY})),
]
