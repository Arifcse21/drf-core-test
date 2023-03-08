from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=155, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
