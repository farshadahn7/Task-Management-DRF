from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user.is_staff)
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        else:
            return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        else:
            return False
