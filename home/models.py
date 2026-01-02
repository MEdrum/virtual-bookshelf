import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    userID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length = 36, unique=True)
    password = models.CharField(max_length = 100)
    email = models.CharField(max_length = 254, unique=True)
    admin = models.BooleanField(default=False)
    groups = None
    user_permissions = None

    def __str__(self):
        return self.username

