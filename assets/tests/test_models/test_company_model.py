import pytest
from assets.models import Company
pytestmark = pytest.mark.django_db


class TestCompanyModel:

    def test_empty_company_model(self):
        count = Company.objects.count()

        assert count == 0

    def test_company_model(self, company_data):
        count = Company.objects.count()

        assert count == 1


