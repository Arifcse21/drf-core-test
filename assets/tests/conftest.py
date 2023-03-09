import pytest
from assets.models import Asset, Company
from rest_framework.test import APIClient
from django.urls import reverse


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


@pytest.fixture(scope="session")
def api_client():
    return APIClient


@pytest.fixture
def company_response(api_client):
    ep = reverse('create-company-list')
    payload = {
        "name": "REPLIQ limited",
        "email": "test@reqliq.dev",
        "phone": "0123567899",
        "address": "Lalmatia, Dhaka"
    }
    response = api_client().post(ep, payload)
    return response


@pytest.fixture
def assets_response(company_response, api_client):
    ep = reverse('create-asset-list')
    payload = {
        "asset_name": "Smart Watch",
        "asset_model": "Apple er watch gular model ki? janina!",
        "asset_of_company_id": "1",
    }
    response = api_client().post(ep, payload)
    return response
