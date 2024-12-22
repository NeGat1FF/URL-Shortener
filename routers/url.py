from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from app.schemas.url import *
from app.utils.url import *
from app.service.url import *

router = APIRouter()

@router.get("/")
async def root():
    # Redirect to the documentation
    return RedirectResponse(url="/docs")

@router.post("/", response_model=Url, description="Create a new short URL")
async def create_url(url: CreateUrl):
    res = await create_short_url(url.url)
    return res

@router.patch("/{shortCode}", response_model=Url, description="Update a short URL")
async def update_url(shortCode: str, url: CreateUrl):
    res = await update_short_url(shortCode, url.url)
    return res

@router.get("/{shortCode}", description="Go to a website using a short URL")
async def go_to_url(shortCode: str):
    res = await get_original_url(shortCode)
    if res is None:
        return HTTPException(status_code=404, detail="URL not found")
    await update_visit_count(shortCode)
    return RedirectResponse(url=res.url)
    
@router.get("/{shortCode}/info", response_model=Url, description="Get information about a short URL")
async def get_url_info(shortCode: str):
    res = await get_original_url(shortCode)
    if res is None:
        return HTTPException(status_code=404, detail="URL not found")
    return res

@router.delete("/{shortCode}", response_model=Url, description="Delete a short URL")
async def delete_url(shortCode: str):
    res = await delete_short_url(shortCode)
    return res