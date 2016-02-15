from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Define models here
class User(AbstractUser):
    """docstring for USER"""
    address1 = models.TextField(null = True, blank = True)
    address2 = models.TextField(null = True, blank = True)
    birth = models.DateTimeField(null = True, blank = True)
    phone_number = models.TextField(null = True, blank = True)


    # Address = models.TextField(null = True, blank = True)
    # City = models.TextField(null = True, blank = True)
    # State = models.TextField(null = True, blank = True)
    # Zip = models.TextField(null = True, blank = True)
    # Birth = models.DateTimeField(null = True, blank = True)
    # PhoneNumber = models.TextField(null = True, blank = True)
    # CCdigits = models.TextField(null = True, blank = True)
    # CCexpiration = models.TextField(null = True, blank = True)
    # CCCVC = models.TextField(null = True, blank = True)

admin.site.register(User)
