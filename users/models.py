import uuid
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


def validate_user_email_null_check(email):
    return None if not email else email

# Create your models here.
class UserModel(AbstractBaseUser):
    USERNAME_FIELD = "email_id"

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