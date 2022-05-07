from rest_framework.permissions import IsAuthenticated


class IsOwnOnly(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user