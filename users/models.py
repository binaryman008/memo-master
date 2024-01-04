import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


def validate_user_email_null_check(email):
    return None if not email else email


class CustomUserManager(BaseUserManager):
    def create_user(self, email_id, password=None, **extra_fields):
        if not email_id:
            raise ValueError('The Email field must be set')
        email_id = self.normalize_email(email_id)
        user = self.model(email_id=email_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email_id, password, **extra_fields)

# Create your models here.
class UserModel(AbstractUser):

    username=None
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(max_length=100, null=True, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=False)
    email_id = models.EmailField(
        max_length=100,
        null=True,
        blank=True,
        unique=True,
        validators=[validate_user_email_null_check],
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email_id"
    objects = CustomUserManager()
