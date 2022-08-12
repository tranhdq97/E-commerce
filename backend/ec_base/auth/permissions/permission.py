from rest_framework.permissions import IsAuthenticated

from ...common.constant.master import MasterStaffID


class IsEmployee(IsAuthenticated):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.type_id == MasterStaffID.EMPLOYEE


class IsManager(IsAuthenticated):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.type_id == MasterStaffID.MANAGER


class IsSuperStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.type_id == MasterStaffID.SUPER_STAFF


class IsApproved(IsAuthenticated):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.is_staff and \
               request.user.type_id != MasterStaffID.UNAPPROVED


class IsStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.is_staff


class IsCustomer(IsAuthenticated):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and not request.user.is_staff
