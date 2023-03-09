from django.db import models
from .company_model import Company


def maintain_serial():
    last = Asset.objects.all().order_by("id").last()
    if last:
        return last.id + 1
    return 1


class Asset(models.Model):
    id = models.AutoField(primary_key=True, editable=False, default=maintain_serial)
    asset_name = models.CharField(max_length=100, null=False, blank=False)
    asset_model = models.CharField(max_length=100, null=False, blank=False)
    asset_of_company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}-{self.asset_name}:{self.asset_model}"


