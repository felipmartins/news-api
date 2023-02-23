from sqlmodel import create_engine, Session, SQLModel
from sqlmodel.pool import StaticPool
from unittest.mock import patch
from news.main import app
from fastapi.testclient import TestClient
from news.db import populate_table


client = TestClient(app)


def get_session_override():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    session = Session(engine)
    populate_table(session)

    return session


def test_get_news():
    with patch("news.main.get_session", get_session_override):
        res = client.get("/news/")
        assert res.status_code == 200
        data = res.json()
        assert data["total_pages"] == 5
