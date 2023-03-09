from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from employee.models import GadgetHandout
from employee.serializers import UpdateGadgetReturnSerializer
from drf_yasg.utils import swagger_auto_schema


class GadgetReturnView(ViewSet):
    @swagger_auto_schema(
        request_body=UpdateGadgetReturnSerializer,
        operation_summary="Employee return a gadget to company record",
        operation_description="This api endpoints take gadget return information and add it to the database"
    )
    def update(self, request, pk=None):
        try:
            queryset= GadgetHandout.objects.filter(pk=pk)
            gadget = queryset.first()
            serializer = UpdateGadgetReturnSerializer(gadget, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                "error": False,
                "status_code": status.HTTP_200_OK,
                "message": "Gadget is returned",
                "data": serializer.data
            }
            return Response(api_response, status=status.HTTP_200_OK)
        except Exception as e:
            api_response = {
                "error": False,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": str(e)
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)

