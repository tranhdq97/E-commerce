from django.urls import path

from ec_base.common.constant.view_action import BaseViewAction
from ec_staff.rating.views.viewset import RatingViewSet

urlpatterns = [
    path("list", RatingViewSet.as_view({"get": BaseViewAction.LIST})),
    path("create", RatingViewSet.as_view({"post": BaseViewAction.CREATE})),
    path("<int:pk>/update", RatingViewSet.as_view({"put": BaseViewAction.UPDATE})),
    path("<int:pk>/detail", RatingViewSet.as_view({"get": BaseViewAction.RETRIEVE})),
    path("<int:pk>/delete", RatingViewSet.as_view({"delete": BaseViewAction.DESTROY})),
]
