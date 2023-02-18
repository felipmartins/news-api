import json
from sqlmodel import SQLModel, create_engine, select, Session
from .model import News

sqlite_file_name = "db.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_table():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)


def populate_table(session):
    with open("mocks/news.json") as file:
        news = json.load(file)
        for each_new in news:
            new = News(**each_new)
            session.add(new)
            session.commit()


def is_table_empty(session, model):
    return session.exec(select(model)).first() is None

def select_query_from_table(session, model, category=None):
    with session as session:
        return select(News).where(News.category == category.lower()) if category else select(News)