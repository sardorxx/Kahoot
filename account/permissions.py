from rest_framework import permissions


class IsAdminOrTargetTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow admin users to access the view
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Allow admin users to access the object if the target user is a teacher
        if request.user.is_staff and obj.user_type == 'Teacher':
            return True
        return False
