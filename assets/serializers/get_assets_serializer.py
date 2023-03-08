from rest_framework.serializers import ModelSerializer, SerializerMethodField
from assets.models import Asset, Company


class GetAssetsSerializer(ModelSerializer):
    company_name = SerializerMethodField("get_company_name")

    class Meta:
        model = Asset
        exclude = "company_name"

    def get_company_name(self, instance):
        company_id = instance.company_name
        try:
            queryset = Company.objects.filter(id=company_id)
            queryset = queryset.first()
            company_name = queryset.name
            return company_name
        except Exception as e:
            return str(e)

