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
        """
        using this method, for register users.

        Args:
        ---------------------------------------
            Args1:str
                    username:users enter their usernames

            Args1:str
                    phone_number:users enter their phone_numbers

            Args1:str
                    password:users enter their passwords

        Returns:
        ------------------------------------------
            if the username and password are correct, we will return the access token and refresh token

        Raises
        --------------------------------------------
            incorrect password: if the password entered by user is incorrect raises validationerror with 400 status code
            inactive user: if the user is inactive raises validationerror with 403 status code
        """
        ser_data = RegisterSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            logger.info(f"the{ser_data['phone_number']} and {ser_data['username']} save in cache for 360 s")
            return Response({'detail': User.sub_login(**ser_data.data)}, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(viewsets.ViewSet):
    permission_classes = []
    
    def create(self, request):
        """
        using this method, for login to system

        Args:
        ------------------------------------
            Args1:str 
                    username:users enter their username

            Args2:str
                    password:users enter their password

        Returns:
        ------------------------------------
            if the username and password are correct, we will return the access token and refresh token
         -----------------------------------------------------
        Raise
        -------------------------------
        incorrect password: if the password entered by user is incorrect raises validationerror with 400 status code
        inactive user: if the user is inactive raises validationerror with 403 status code
        """
        ser_data = LoginSerializer(data=request.data)
        if ser_data.is_valid():
            user = get_object_or_404(User, username=ser_data.data['username'])
            logger.info('the tokens return to user')
            return Response({'detail': user.login(ser_data.data['password'])}, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmViewSet(viewsets.ViewSet):
    def create(self, request):
        """
        this function is used for confirmation phone number for register or login

        Parameters
        ====================================
        arg1 :str
                username:front send the username

        arg2:str
                phone_number:front send the phone number 

        arg3:str
                code:users enter the code that sent to their phone numbers
         
        Returns
        ====================================
        if the code entered by the user is correct and the user wants to register,
        we return a message with the following content:
        the user is registered.

        if the code entered by the user is correct and the user wants to login,
        we return refresh token and access token.

        Raises
        ====================================
        incorrect code: if the code entered by the user is not correct raises validationerror with 400 status code
        try register: If the phone number and username have not been sent the registration request 
        raises validationerror with 408 status code
        """
        ser_data = ConfirmSerializer(data=request.data)
        if ser_data.is_valid():
            logger.info(f"the {ser_data.data['phone_number']} is verified")
            return Response({'detail': User.confirm(**ser_data.data)},
                            status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)