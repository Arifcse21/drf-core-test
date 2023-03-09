from django.db import models
import uuid
from assets.models import Company


class Employee(models.Model):
    full_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField()
    employer = models.ForeignKey(Company, related_name="company_name", on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
