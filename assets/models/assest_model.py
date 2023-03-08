from django.db import models
from .company_model import Company


class Asset(models.Model):
    asset_name = models.CharField(max_length=100, null=False, blank=False)
    asset_model = models.CharField(max_length=100, null=False, blank=False)
    asset_stock = models.IntegerField()
    asset_of_company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}:{self.model}-{self.stock}"


