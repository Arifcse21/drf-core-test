from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from assets.serializers import CompanySerializer
from assets.models import Company
from drf_yasg.utils import swagger_auto_schema


class GetCompanyView(ViewSet):
    @swagger_auto_schema(
        operation_summary="Get all company list",
        operation_description="This api endpoint list all the companies in the database"
    )
    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        api_response = {
            "error": False,
            "status_code": status.HTTP_200_OK,
            "message": "All companies list",
            "data": serializer.data
        }
        return Response(api_response, status=status.HTTP_200_OK)
