from rest_framework import permissions


class IsBroker(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return bool(request.user and request.user.role_set.get().role == 1)

        return True
