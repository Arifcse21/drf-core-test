from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from assets.serializers import CompanySerializer
from assets.models import Company
from drf_yasg.utils import swagger_auto_schema


class IndividualCompanyView(ViewSet):
    @swagger_auto_schema(
        operation_summary="Get individual company record",
        operation_description="This api endpoint fetch individual company data from the database"
    )
    def retrieve(self, request, pk=None):
        queryset = Company.objects.filter(pk=pk).first()
        serializer = CompanySerializer(queryset)
        api_response = {
            "error": False,
            "status_code": status.HTTP_200_OK,
            "message": "Individual company data",
            "data": serializer.data
        }
        return Response(api_response, status=status.HTTP_200_OK)
