from app.db.connection import get_db_connection
from app.utils.url import generate_random_string
from app.schemas.url import Url



async def create_short_url(original_url: str):
    short_code = generate_random_string()
    query = """
    INSERT INTO urls (url, short_code)
    VALUES (%s, %s)
    RETURNING *;
    """
    async with get_db_connection() as cur:
        await cur.execute(query, (str(original_url), short_code))
        result = await cur.fetchone()
        await cur.close()
    return Url.model_validate(result)

async def get_original_url(short_code: str):
    query = "SELECT * FROM urls WHERE short_code = %s;"
    async with get_db_connection() as cur:
        await cur.execute(query, (short_code,))
        result = await cur.fetchone()
    return Url.model_validate(result)

async def update_short_url(short_code: str, original_url: str):
    query = "UPDATE urls SET url = %s, updated_at = NOW() WHERE short_code = %s RETURNING *;"
    async with get_db_connection() as cur:
        await cur.execute(query, (original_url, short_code))
        result = await cur.fetchone()
    return Url.model_validate(result)

async def delete_short_url(short_code: str):
    query = "DELETE FROM urls WHERE short_code = %s;"
    async with get_db_connection() as cur:
        await cur.execute(query, (short_code,))

async def update_visit_count(short_code: str):
    query = "UPDATE urls SET visit_count = visit_count + 1 WHERE short_code = %s;"
    async with get_db_connection() as cur:
        await cur.execute(query, (short_code,))