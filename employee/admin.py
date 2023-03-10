from django.contrib import admin
from .models import (
    Employee,
    GadgetHandout
)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "full_name",
        "email",
        "employer",
        "created_at",
        "modified_at",
        "is_active",
    ]


@admin.register(GadgetHandout)
class GadgetHandoutAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "employee_id",
        "gadget_id",
        "employer_id",
        "checked_out_at",
        "created_at",
        "modified_at",
        "is_returned",
        "returned_at",
    ]

