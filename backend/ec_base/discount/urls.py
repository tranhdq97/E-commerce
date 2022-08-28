from django.urls import path

from .views.viewset import DiscountViewSet
from ..common.constant.view_action import BaseViewAction

urlpatterns = [
    path('list', DiscountViewSet.as_view({'get': BaseViewAction.LIST})),
    path('create', DiscountViewSet.as_view({'post': BaseViewAction.CREATE})),
    path('<int:pk>/update', DiscountViewSet.as_view({'put': BaseViewAction.UPDATE})),
    path('<int:pk>/detail', DiscountViewSet.as_view({'get': BaseViewAction.RETRIEVE})),
    path('<int:pk>/destroy', DiscountViewSet.as_view({'delete': BaseViewAction.DESTROY})),
]
