import pytest
from assets.models import Asset, Company

pytestmark=pytest.mark.django_db


class TestAssetModel:
    def test_empty_asset_model(self):
        count = Asset.objects.count()
        assert count == 0

    def test_asset_model(self, company_data):
        Asset.objects.create(
            asset_name="Laptop",
            asset_model="Asus-x556uq",
            asset_of_company_id=company_data,
        )
        query = Asset.objects.all()
        count = query.count()
        asset = query.get(pk=1)

        assert count == 1
        assert asset.asset_name == "Laptop"
        assert asset.asset_of_company_id == company_data










