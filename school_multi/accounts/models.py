from django.contrib.auth.models import AbstractUser
from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    domain = models.CharField(max_length=255, unique=True, null=True, blank=True)


    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLE_CHOICES = (
        ('master_admin', 'Master Admin'),
        ('director', 'Director'),
        ('staff', 'Staff'),
        ('teacher', 'Teacher'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
