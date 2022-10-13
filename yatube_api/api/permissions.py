from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Проверка на автора
    """

    message = "Вы не являетесь автором контента"

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
