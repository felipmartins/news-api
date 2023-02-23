from typing import Optional
from sqlmodel import SQLModel, Field


class News(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    author: str = Field(max_length=50)
    title: str = Field(max_length=100)
    content: str = Field(max_length=5000)
    category: str = Field(max_length=50)
    timestamp: str = Field(max_length=50)
