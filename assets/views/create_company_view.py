from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from assets.serializers import CompanySerializer
from drf_yasg.utils import swagger_auto_schema


class CreateCompanyView(ViewSet):
    @swagger_auto_schema(
        request_body=CompanySerializer,
        operation_summary="create/add a new company",
        operation_description="This api endpoint creates a company with required data"
    )
    def create(self, request):
        print("company_data = ", request.data)
        try:
            create_company_data = {
                "name": request.data["name"],
                "email": request.data["email"],
                "phone": request.data["phone"],
                "address": request.data["address"]
            }
            serializer = CompanySerializer(data=create_company_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            api_response = {
                "error": False,
                "message": f"{request.data['name']} is added as a company",
                "status_code": status.HTTP_201_CREATED,
                "data": serializer.data
            }
            return Response(api_response, status=status.HTTP_201_CREATED)

        except Exception as e:
            api_response = {
                "error": True,
                "message": str(e),
                "status_code": status.HTTP_400_BAD_REQUEST,
            }
            return Response(api_response, status=status.HTTP_201_CREATED)


