from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, phone_number, password):
        if not username:
            raise ValueError('you must have username')

        if not phone_number:
            raise ValueError('you must have phone_number')

        user = self.model(username=username, phone_number=phone_number)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, phone_number, password):
        user = self.create_user(username, phone_number, password)
        user.is_admin = True
        user.save(using=self.db)
        return user