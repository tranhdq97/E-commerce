from django.urls import path

from .views.viewset import RatingViewSet
from ..common.constant.view_action import BaseViewAction

urlpatterns = [
    path('list', RatingViewSet.as_view({'get': BaseViewAction.LIST})),
    path('create', RatingViewSet.as_view({'post': BaseViewAction.CREATE})),
    path('<int:pk>/update', RatingViewSet.as_view({'put': BaseViewAction.UPDATE})),
    path('<int:pk>/detail', RatingViewSet.as_view({'get': BaseViewAction.RETRIEVE})),
]
