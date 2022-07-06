from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=False,null=True)
    last_name = models.CharField(unique=False,null=True,max_length=255)