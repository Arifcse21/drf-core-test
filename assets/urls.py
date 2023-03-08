from rest_framework.routers import DefaultRouter
from assets.views import (
    CreateCompanyView,
    GetCompanyView,
    UpdateCompanyView,
    DeleteCompanyView,
    IndividualCompanyView
)
from django.urls import path, include


router = DefaultRouter()

# Create Company
router.register("create-company", CreateCompanyView, basename="create-company")
# Get all company
router.register("company-list", GetCompanyView, basename="get-all-company")
# Update company
router.register("update-company", UpdateCompanyView, basename="update-company")
# Delete company
router.register("delete-company", DeleteCompanyView, basename="delete-company")
# Individual company
router.register("individual-company", IndividualCompanyView, basename="individual-company")


urlpatterns = [
    path("api/v1/assets/", include(router.urls))
]

