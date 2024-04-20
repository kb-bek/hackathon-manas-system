from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

from user.managers import CustomUserManager


class User(AbstractUser):
    first_name = models.CharField(
        max_length=30,
        blank=False
    )

    last_name = models.CharField(
        max_length=30,
        blank=False
    )

    father_name = models.CharField(
        max_length=30,
        blank=False
    )

    date_of_birth = models.DateTimeField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        blank=True
    )

    citizenship = models.CharField(
        max_length=15,
        blank=True
    )

    email = models.EmailField(
        unique=True,
    )

    phone_number = models.CharField(
        max_length=15,
        blank=False,
    )

    password = models.CharField(
        max_length=20,
        blank=False
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()
