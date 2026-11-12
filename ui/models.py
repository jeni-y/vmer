from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class VirtualMachine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vm_name = models.CharField(max_length=30)
    ssh_public_key = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
