from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not username:
            raise ValueError('you must have username')

        if not email:
            raise ValueError('you must have email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self.db)
        return user