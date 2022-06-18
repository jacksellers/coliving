from rest_framework import permissions

class UserPermission(permissions.AllowAny):
    
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_staff
        elif view.action == 'create':
            return True
        else:
            return False
