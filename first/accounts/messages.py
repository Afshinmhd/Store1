from enum import Enum
from django.utils.translation import gettext as _



class Messages(Enum):

    DUPLICATE_MOBILE_NUMBER = _('There is a user with this mobile number')
    INCORRECT_CODE = _('The code entered is incorrect')
    EDIT_INFORMATION = _('User information is incorrect')
    NOT_FOUND_USER = _('This user does not exist')
    INACTIVE_USER = _('User is not active')
    INCORRECT_PASSWORD = _('Password is incorrect')
    INCORRECT_PHONE_NUMBER = _('Mobile number is incorrect')
    SEND_CODE = _('Verification code sent to you')
    TTL_ERROR = _('try {} another seconds')
    INCORRECT_MOBILE =  _('Mobile number is being used by another user')
    INCORRECT_USERNAME = _('Username is being used by another user')
    LOGIN_ERROR = _('You are logged in')
    LOGOUT = _('You are logged out')
    CHANGE_PASSWORD = _('Password changed successfully')
    REPEAT_NEW_PASSWORD = _('Passwords are not the same')
