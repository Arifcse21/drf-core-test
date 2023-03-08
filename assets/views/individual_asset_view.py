from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from assets.serializers import GetAssetsSerializer
from assets.models import Asset
from drf_yasg.utils import swagger_auto_schema


class IndividualAssetView(ViewSet):
    @swagger_auto_schema(
        operation_summary="Get individual asset record",
        operation_description="This api endpoint fetch individual asset data from the database"
    )
    def retrieve(self, request, pk=None):
        queryset = Asset.objects.filter(pk=pk).first()
        serializer = GetAssetsSerializer(queryset)
        api_response = {
            "error": False,
            "status_code": status.HTTP_200_OK,
            "message": "Individual asset data",
            "data": serializer.data
        }
        return Response(api_response, status=status.HTTP_200_OK)
