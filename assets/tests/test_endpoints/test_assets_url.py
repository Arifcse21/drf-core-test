import pytest
from django.urls import reverse
pytestmark = pytest.mark.django_db


class TestAssetsUrl:

    @pytest.mark.xfail
    def test_will_fail(self, api_client):
        ep = reverse("create-asset-list")
        payload = {}        # No payload will raise exception
        resp = api_client().post(ep, payload)

        assert resp.status_code == 201

    def test_create_asset_url(self, assets_response):
        resp = assets_response
        assert resp.status_code == 201

    def test_delete_asset_url(self, api_client, assets_response):
        delete_ep = reverse("delete-asset-detail", kwargs={"pk": 1})

        resp = api_client().delete(delete_ep)

        assert resp.status_code == 200
        response = resp.json()
        assert response["error"] is False
        assert response["status_code"] == resp.status_code
        


