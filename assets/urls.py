from rest_framework.routers import DefaultRouter
from assets.views import (
    CreateCompanyView,
    GetCompanyView,
    UpdateCompanyView,
    DeleteCompanyView,
    IndividualCompanyView,

    CreateAssetsView,
    DeleteAssetsView,
    GetAllAssetOfCompanyView,
    IndividualAssetView,
    UpdateAssetView,
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

# Create assets
router.register("create-asset", CreateAssetsView, basename="create-asset")
# Delete assets
router.register("delete-asset", DeleteAssetsView, basename="delete-asset")
# Get company's assets
router.register("company-assets", GetAllAssetOfCompanyView, basename="company-assets")
# Individual asset
router.register("individual-asset", IndividualAssetView, basename="individual-asset")
# Update asset
router.register("update-asset", UpdateAssetView, basename="update-asset")


urlpatterns = [
    path("api/v1/assets/", include(router.urls))
]

