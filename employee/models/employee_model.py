from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from assets.models import Company


class Employee(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4(), editable=False)
    employer = models.ForeignKey(Company, related_name="company_name",on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
