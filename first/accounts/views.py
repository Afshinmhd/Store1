import logging
from rest_framework import viewsets, status
from .models import User
from .serializers import RegisterSerializer, LoginSerializer ,ConfirmSerializer
from rest_framework.response import Response
from .permissions import IsOwnOnly
from django.shortcuts import get_object_or_404


logger = logging.getLogger(__name__)

class RegisterViewSet(viewsets.ViewSet):
    permission_classes = []
    queryset = User.objects.all()

    def create(self, request):
        ser_data = RegisterSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            logger.info(f"the{ser_data['phone_number']} and {ser_data['username']} save in cache for 360 s")
            return Response({'detail': User.sub_login(**ser_data.data)}, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(viewsets.ViewSet):
    permission_classes = []
    
    def create(self, request):
        ser_data = LoginSerializer(data=request.data)
        if ser_data.is_valid():
            user = get_object_or_404(User, username=ser_data.data['username'])
            logger.info('the tokens return to user')
            return Response({'detail': user.login(ser_data.data['password'])}, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmViewSet(viewsets.ViewSet):
    def create(self, request):
        ser_data = ConfirmSerializer(data=request.data)
        if ser_data.is_valid():
            logger.info(f"the {ser_data.data['phone_number']} is verified")
            return Response({'detail': User.confirm(**ser_data.data)},
                            status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)