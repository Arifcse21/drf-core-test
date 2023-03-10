from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from employee.models import Employee
from employee.serializers import CreateEmployeeSerializer
from drf_yasg.utils import swagger_auto_schema


class CreateEmployeeView(ViewSet):
    @swagger_auto_schema(
        request_body=CreateEmployeeSerializer,
        operation_summary="Create/add new employee of a company",
        operation_description="This api endpoints take employee information and add it to the company"
    )
    def create(self, request):
        try:
            serializer = CreateEmployeeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                "error": False,
                "status_code": status.HTTP_201_CREATED,
                "message": "New employee added",
                "data": serializer.data
            }
            return Response(api_response, status=status.HTTP_201_CREATED)

        except Exception as e:
            api_response = {
                "error": True,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": str(e),
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)
