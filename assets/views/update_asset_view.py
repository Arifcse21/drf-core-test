from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from assets.serializers import CreateAssetsSerializer
from assets.models import Asset
from drf_yasg.utils import swagger_auto_schema


class UpdateAssetView(ViewSet):
    @swagger_auto_schema(
        request_body=CreateAssetsSerializer,
        operation_summary="update asset info",
        operation_description="This api endpoint update an asset data"
    )
    def update(self, request, pk=None):
        queryset = Asset.objects.filter(pk=pk)
        asset = queryset.first()
        try:
            serializer = CreateAssetsSerializer(asset, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                "error": False,
                "status_code": status.HTTP_200_OK,
                "message": "Asset data updated",
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

