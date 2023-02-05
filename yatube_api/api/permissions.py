from rest_framework.permissions import (SAFE_METHODS, BasePermission,
                                        IsAuthenticatedOrReadOnly)

# Полностью переделал permissions, чтобы убрать переопределение def get_permissions 
# во views.py и оставить один Permission.
# Соответственно, и код станет проще, и будет учтено замечание из ревью
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
