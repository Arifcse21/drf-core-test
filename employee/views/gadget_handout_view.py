from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from employee.models import Employee
from employee.serializers import CreateGadgetHandoutSerializer
from drf_yasg.utils import swagger_auto_schema


class GadgetHandoutView(ViewSet):
    @swagger_auto_schema(
        request_body=CreateGadgetHandoutSerializer,
        operation_summary="Create/add new gadget handout to an employee record",
        operation_description="This api endpoints take gadget handout information and add it to the database"
    )
    def create(self, request):
        try:
            serializer = CreateGadgetHandoutSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            api_response = {
                "error": False,
                "status_code": status.HTTP_201_CREATED,
                "message": "Gadget handout to employee",
                "data": serializer.data
            }
            return Response(api_response, status=status.HTTP_201_CREATED)
        except Exception as e:
            api_response = {
                "error": False,
                "status_code": status.HTTP_201_CREATED,
                "message": str(e),
            }
            return Response(api_response, status=status.HTTP_201_CREATED)
