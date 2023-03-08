from rest_framework.serializers import ModelSerializer, SerializerMethodField
from assets.models import Asset, Company


class GetAssetsSerializer(ModelSerializer):
    asset_of_company_name = SerializerMethodField("get_company_name")

    class Meta:
        model = Asset
        fields = "__all__"

    def get_company_name(self, instance):
        company_name = instance.asset_of_company_id
        return str(company_name)

