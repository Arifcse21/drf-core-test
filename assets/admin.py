from django.contrib import admin
from .models import (Company, Asset)
# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "phone",
        "created_at",
        "modified_at",
        "is_active",
    ]


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "asset_name",
        "asset_model",
        "asset_of_company_id",
        "created_at",
        "modified_at"
    ]
