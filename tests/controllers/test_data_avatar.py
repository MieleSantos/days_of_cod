from fastapi import status
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_sucess_get_avatar_data():
    response = client.get("/avatar/")
    assert response.status_code == status.HTTP_200_OK
