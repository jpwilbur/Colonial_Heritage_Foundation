from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Define models here
class User(AbstractUser):
    """docstring for USER"""

    address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()
    birth = models.DateTimeField()
    phoneNumber = models.TextField()
    ccDigits = models.TextField(null = True, blank = True)
    ccExpiration = models.TextField(null = True, blank = True)
    ccCVC = models.TextField(null = True, blank = True)

admin.site.register(User)
