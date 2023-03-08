from django.db import models
from .employee_model import Employee
from assets.models import Asset, Company


class GadgetHandout(models.Model):
    employee_id = models.ForeignKey(Employee, related_name="employee_name",on_delete=models.CASCADE)
    gadget_id = models.ForeignKey(Asset, on_delete=models.DO_NOTHING, null=True, blank=True)
    employer_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    checked_out_at = models.DateField()
    is_returned = models.BooleanField(default=False)
    returned_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee_id
