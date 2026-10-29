from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class Sigup(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(
        max_length=10,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Phone number must be exactly 10 digits.'
            )
        ]
    )

    REQUIRED_FIELDS = ['email', 'phone_number']

class VmRequirements(models.Model):
    vm_name = models.CharField(max_length=50, unique=True)
    ssh_key = models.CharField(max_length=500)
    username =models.ForeignKey(Sigup, to_field='username' , on_delete=models.CASCADE)