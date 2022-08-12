from django.urls import path

from .views.viewset import ProductViewSet
from ..common.constant.view_action import BaseViewAction

urlpatterns = [
    path('create', ProductViewSet.as_view({'post': BaseViewAction.CREATE})),
    path('list', ProductViewSet.as_view({'get': BaseViewAction.LIST})),
    path('<int:pk>/detail', ProductViewSet.as_view({'get': BaseViewAction.RETRIEVE})),
    path('<int:pk>/delete', ProductViewSet.as_view({'delete': BaseViewAction.DESTROY})),
    path('<int:pk>/update', ProductViewSet.as_view({'put': BaseViewAction.UPDATE})),
]
