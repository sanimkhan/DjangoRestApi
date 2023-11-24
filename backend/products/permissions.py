from rest_framework import permissions


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='customer').exists()


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='admin').exists()


class IsCustomerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['customer', 'admin']).exists()
