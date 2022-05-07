from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from django.utils.translation import gettext as _
from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework import status
from .utils import otp_code
from .messages import Messages
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    email = models.EmailField(_('email'), max_length=255, unique=True)
    phone_number = models.CharField(_('phone_number'), max_length=11, unique=True, 
                                        null=True, blank=True)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_verified = models.BooleanField(_('is_verified'),default=True)
    is_admin = models.BooleanField(_('is_admin'),default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    def __str__(self):
        return self.username

    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def login(username, phone_number):
        if cache.get(f'code_{phone_number}'):
            ttl = cache.ttl(f'code_{phone_number}')
            raise ValidationError(Messages.TTL_ERROR.value.format(ttl))
        elif not cache.get(f'username_{phone_number}'):
            cache.set_many({f'phone_number_{phone_number}': phone_number,
                            f'username_{username}': username}, 300)
        
        code = otp_code(f'code_{phone_number}', code, 60)
        return status.HTTP_200_OK, Messages.SEND_CODE.value

    def confirm(username, phone_number, code):
        if cache.get(f'username_{phone_number}') != username:
            raise ValidationError(Messages.EDIT_INFORMATION.value)
        elif cache.get(f'code_{phone_number}') != code:
            raise ValidationError(Messages.INCORRECT_CODE.value)
        person = User.objects.get_or_create(
            username=username, phone_number=phone_number, is_verified=True
        )
        cache.delete_many([person[0].pk, f'code_{phone_number}'])
        return (status.HTTP_200_OK, {person[0].get_token_for_user()['refresh'],
                person[0].get_token_for_user()['access']})
