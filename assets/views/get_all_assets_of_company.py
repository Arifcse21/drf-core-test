from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from assets.serializers import GetAssetsSerializer
from assets.models import Asset
from drf_yasg.utils import swagger_auto_schema


class GetAllAssetOfCompanyView(ViewSet):
    @swagger_auto_schema(
        operation_summary="Get all assets of a company",
        operation_description="This api endpoint list all the assets of a company in the database"
    )
    def retrieve(self, request, pk=None):
        try:
            queryset = Asset.objects.filter(asset_of_company_id=pk)
            serializer = GetAssetsSerializer(queryset, many=True)
            api_response = {
                "error": False,
                "status_code": status.HTTP_200_OK,
                "message": "Company's all assets list",
                "data": serializer.data
            }
            return Response(api_response, status=status.HTTP_200_OK)
        except Exception as e:
            api_response = {
                "error": True,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": str(e),
            }
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)


