from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from assets.serializers import CompanySerializer
from assets.models import Company
from drf_yasg.utils import swagger_auto_schema


class DeleteCompanyView(ViewSet):
    @swagger_auto_schema(
        operation_summary="Delete a company record",
        operation_description="This api endpoint bulk delete a company from the database"
    )
    def destroy(self, request, pk=None):
        try:
            Company.objects.get(pk=pk).delete()
            api_response = {
                "error": False,
                "status_code": status.HTTP_200_OK,
                "message": f"company with {pk} deleted",
            }
            return Response(api_response, status=status.HTTP_200_OK)
        except Exception as e:
            api_response = {
                "error": True,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": str(e),
            }
            return Response(api_response, status=status.HTTP_404_NOT_FOUND)

