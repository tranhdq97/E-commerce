from rest_framework.permissions import IsAuthenticated

from ec_base.common.constant.auth import UserEnum
from ec_base.common.constant.master import MasterStaffTypeID, MasterCustomerTypeID


class IsStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.provider == UserEnum.STAFF


class IsEmployee(IsStaff):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.type_id == MasterStaffTypeID.EMPLOYEE


class IsManager(IsStaff):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.type_id == MasterStaffTypeID.MANAGER


class IsSuperStaff(IsStaff):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.type_id == MasterStaffTypeID.SUPER_STAFF


class IsApproved(IsStaff):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.type_id != MasterStaffTypeID.UNAPPROVED


class IsCustomer(IsAuthenticated):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.provider == UserEnum.CUSTOMER


class IsVerified(IsCustomer):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.type_id == MasterCustomerTypeID.VERIFIED


class IsUnverified(IsCustomer):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.type_id == MasterCustomerTypeID.UNVERIFIED
