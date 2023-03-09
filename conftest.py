import pytest
from assets.models import Asset, Company


@pytest.fixture
def company_data(db):
    company = Company.objects.create(
        name="test_company",
        email="test@test.com",
        phone="0122222223",
        website="https://test.com",
        address="Dhaka-1200"
    )
    return company




