from rest_framework import permissions


class IsDoctorPermission(permissions.BasePermission):
    message = 'You must be a doctor to access this resource.'

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
                request.user.groups.filter(name='doctor').exists() or request.user.is_staff
        )
