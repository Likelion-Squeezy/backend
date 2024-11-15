from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(("email address"), blank=True, unique=True)
    eezy_count = models.IntegerField(default=20)
    squeezy_count = models.IntegerField(default=10)