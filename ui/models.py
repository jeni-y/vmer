from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class Sigup(models.Model):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
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
    password = models.CharField(max_length=100,validators=[MinLengthValidator(8)])