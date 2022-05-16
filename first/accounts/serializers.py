from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from .messages import Messages
from rest_framework.serializers import ValidationError


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True, max_length=60,
        validators=[UniqueValidator(queryset=User.objects.all(),
            message=Messages.INCORRECT_USERNAME.value)])
    phone_number = serializers.SlugField(max_length=11,
        validators=[UniqueValidator(queryset=User.objects.all(),
            message=Messages.INCORRECT_MOBILE.value)])
    password = serializers.CharField(write_only=True)

    def validate_phone_number(self, value):
        if int(value) and value[0:2] == '09':
            return value
        else:
            return ValidationError(Messages.INCORRECT_PHONE_NUMBER.value)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    phone_number = serializers.SlugField(max_length=11)
    code = serializers.CharField(max_length=5)

