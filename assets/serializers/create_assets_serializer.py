from rest_framework.serializers import ModelSerializer
from assets.models import Asset


class CreateAssetsSerializer(ModelSerializer):

    class Meta:
        model = Asset
        fields = "__all__"
