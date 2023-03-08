from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from assets.models import Company


class Employee(AbstractUser):
    employer = models.ForeignKey(Company, related_name="company_name",on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
