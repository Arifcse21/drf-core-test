import pytest
from django.urls import reverse
pytestmark = pytest.mark.django_db


class TestCompanyUrls:

    def test_create_company_url(self, company_response):

        assert company_response.status_code == 201
        response = company_response.json()
        assert response["error"] is False

    def test_update_company_url(self, api_client, company_response):
        ep = reverse("update-company-detail", kwargs={"pk": 1})
        payload = {
            "name": "test-test company",
            "email": "info@repliq.dev",
            "phone": "016777777779",
            "website": "https://repliq.dev",
            "address": "Dhaka-1200"
        }
        resp = api_client().put(ep, payload)

        assert resp.status_code == 200
        response = resp.json()

        assert response["error"] is False
        assert response["status_code"] == resp.status_code
        


