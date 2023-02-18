from fastapi import FastAPI, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from news.db import (
    create_db_and_table,
    populate_table,
    is_table_empty,
    get_session,
    select_query_from_table,
)
from news.model import News


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_response(
    news: list, category_filter: str, current_page: int, total_pages: int
):
    return {
        "total_pages": total_pages,
        "current_page": current_page,
        "category_filter": category_filter,
        "result": news,
    }


@app.on_event("startup")
def on_startup():
    create_db_and_table()
    with get_session() as session:
        if is_table_empty(session, News):
            populate_table(session)


@app.get("/")
async def home():
    return {"detail": "news-api, access /docs for documentation"}


@app.get("/health")
async def health():
    return {"status": "healthy as a healthy horse"}


@app.get("/get_news")
async def evaluation(category: str | None = None, page: int = Query(default=1, gt=0)):
    with get_session() as session:
        query = select_query_from_table(session, News, category)

        number_of_news = len(session.exec(query).all())
        page_news = session.exec(query.offset(12 * (page - 1)).limit(12)).all()

        full_pages, extra = divmod(number_of_news, 12)
        total_pages = full_pages + bool(extra)

    if page == total_pages:
        return create_response(page_news, category, page, total_pages)

    if page < total_pages:
        return create_response(
            page_news,
            category,
            page,
            total_pages,
        )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"page {page} does not exist"
        if not category
        else f"page {page} does not exist for selected filter: {category}",
    )
