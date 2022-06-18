from django.db import models
from django.contrib.auth.models import AbstractUser

from core.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
