from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from .messages import Messages
from rest_framework.serializers import ValidationError


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    phone_number = serializers.SlugField(required=True)

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

class MobileVerificationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=55)
    mobile_number = serializers.SlugField(required=True, max_length=11)
    code = serializers.CharField(required=True)

class EditUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


