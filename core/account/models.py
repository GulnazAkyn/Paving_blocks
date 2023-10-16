from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):

    def create_user(self, username, email, phone, password=None):
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            phone=phone,
            email=email
            )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, phone, password=None):
        user = self.create_user(username, email, phone, password)
        user.is_admin = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=125, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, unique=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


