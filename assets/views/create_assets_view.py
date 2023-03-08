from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from assets.serializers import CreateAssetsSerializer
from drf_yasg.utils import swagger_auto_schema


class CreateAssetsView(ViewSet):
    @swagger_auto_schema(
        request_body=CreateAssetsSerializer,
        operation_summary="create/add an asset of a company",
        operation_description="This api endpoint creates an asset of company with required data"
    )
    def create(self, request):
        try:
            serializer = CreateAssetsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                "error": False,
                "status_code": status.HTTP_201_CREATED,
                "message": "new asset added",
                "data": serializer.data
            }
            return Response(api_response, status=status.HTTP_201_CREATED)
        except Exception as e:
            api_response = {
                "error": False,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": str(e),
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)


