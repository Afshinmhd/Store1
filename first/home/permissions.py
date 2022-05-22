from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser


class IsOwnOrReadOnly(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
         if request.user == IsAdminUser:
             return True