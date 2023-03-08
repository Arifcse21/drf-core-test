from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from assets.serializers import CompanySerializer
from assets.models import Company
from drf_yasg.utils import swagger_auto_schema


class UpdateCompanyView(ViewSet):
    @swagger_auto_schema(
        request_body=CompanySerializer,
        operation_summary="update company info",
        operation_description="This api endpoint update a company data"
    )
    def update(self, request, pk=None):
        queryset = Company.objects.filter(pk=pk)
        company = queryset.first()
        try:
            serializer = CompanySerializer(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                "error": False,
                "status_code": status.HTTP_200_OK,
                "message": "Company data updated",
                "data": serializer.data
            }
            return Response(api_response, status=status.HTTP_200_OK)
        except Exception as e:
            api_response = {
                "error": True,
                "status_code": status.HTTP_304_NOT_MODIFIED,
                "message": str(e),
            }
            return Response(api_response, status=status.HTTP_304_NOT_MODIFIED)

