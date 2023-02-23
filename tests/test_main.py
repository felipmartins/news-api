from news.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_home_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"detail": "news-api, access /docs for documentation"}


def test_get_news():
    response = client.get("/news")
    assert response.status_code == 200
    assert len(response.json()['result']) == 12
    assert response.json()['total_pages'] == 5