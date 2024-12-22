from datetime import datetime
from pydantic import HttpUrl, Field, BaseModel

class Url(BaseModel):
    id: int = Field(int, ge=1)
    url: HttpUrl
    short_code: str = Field(str, min_length=6, max_length=6)
    visit_count: int = Field(int, ge=0)
    created_at: datetime
    updated_at: datetime

class CreateUrl(BaseModel):
    url: HttpUrl

