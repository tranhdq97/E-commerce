from django.urls import path

from ec_base.common.constant.view_action import BaseViewAction
from ec_staff.staff.views.viewset import StaffViewSet

urlpatterns = [
    path("create", StaffViewSet.as_view({"post": BaseViewAction.CREATE})),
    path("update", StaffViewSet.as_view({"put": BaseViewAction.UPDATE})),
]
