from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    RoleChoices = (
        ('CUSTOMER', 'Customer'),
        ('STAFF', 'Staff'),
        ('MANAGER', 'Manager')

    )
    role = models.CharField(max_length=10,choices=RoleChoices)
    phone = models.CharField(max_length=10)
    kyc_verified = models.BooleanField(default=False)
    date = models.DateField()
    