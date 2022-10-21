from django.urls import path

from ec_base.common.constant.view_action import ProductCategoryViewAction
from ec_staff.master.views.product_category import ProductCategoryViewSet

urlpatterns = [
    path("product-category/get-sale-quantity-overview",
         ProductCategoryViewSet.as_view({"get": ProductCategoryViewAction.GET_SALE_QUANTITY_OVERVIEW})),
    path("product-category/get-sale-amount-overview",
         ProductCategoryViewSet.as_view({"get": ProductCategoryViewAction.GET_SALE_AMOUNT_OVERVIEW})),
]
