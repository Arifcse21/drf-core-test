from rest_framework.routers import DefaultRouter
from django.urls import path, include
from employee.views import (
    CreateEmployeeView,
    GadgetHandoutView,
    GadgetReturnView
)

router = DefaultRouter()

# Add new employee
router.register("add-employee", CreateEmployeeView, basename="add-new-employee")
# Handout gadget
router.register("gadget-handout", GadgetHandoutView, basename="gadget-handout-to-emp")
# Return gadget
router.register("return-gadget", GadgetReturnView, basename="return-gadget-to-company")


urlpatterns = [
    path("api/v1/employee/", include(router.urls))
]
