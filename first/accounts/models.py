import logging
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


logger = logging.getLogger(__name__)

class User(AbstractUser):
    phone_number = models.CharField(_('phone_number'), max_length=11, unique=True, 
                                        null=True, blank=True)
    is_verified = models.BooleanField(_('is_verified'),default=True)
    is_admin = models.BooleanField(_('is_admin'),default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def sub_login(username, phone_number):
        if cache.get(f'code_{phone_number}'):
            ttl = cache.ttl(f'code_{phone_number}')
            raise ValidationError(Messages.TTL_ERROR.value.format(ttl))
        elif not cache.get(f'username_{phone_number}'):
            cache.set_many({f'phone_number_{phone_number}': phone_number,
                            f'username_{phone_number}': username}, 300)
        
        code = otp_code()
        print(f'hellllo{code}')
        cache.set(f'code_{phone_number}', code, 60)
        return status.HTTP_200_OK, Messages.SEND_CODE.value

    def login(self, password):
        validate_password = self.check_password
        if not validate_password:
            raise ValidationError(Messages.INCORRECT_PASSWORD.value)
        else:
            cache.delete(self.pk)
            return (status.HTTP_200_OK ,
                    {'refresh': self.get_tokens_for_user()['refresh'],
                     'access': self.get_tokens_for_user()['access']})

    def confirm(username, phone_number, code):
        if not cache.get(f'username_{phone_number}') == username:
            raise ValidationError(Messages.EDIT_INFORMATION.value)
        elif not cache.get(f'code_{phone_number}') == code:
            raise ValidationError(Messages.INCORRECT_MOBILE.value)
        person = User.objects.get_or_create(
            username=username, phone_number=phone_number)
        cache.delete_many([person[0].pk,f'code_{code}'])
        return(status.HTTP_200_OK,
                {'refresh': person[0].get_tokens_for_user()['refresh'],
                'access': person[0].get_tokens_for_user()['access']})

