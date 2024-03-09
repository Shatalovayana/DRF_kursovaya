from rest_framework.permissions import BasePermission


class IsHabitUser(BasePermission):
    """Проверка на владельца привычки"""
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
