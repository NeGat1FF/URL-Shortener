import os
from contextlib import asynccontextmanager
import psycopg
from psycopg.rows import dict_row

@asynccontextmanager
async def get_db_connection():
    conn = await psycopg.AsyncConnection.connect("postgresql://user:pass@localhost:5432/urls", autocommit=True, row_factory=dict_row)
    try:
        yield conn.cursor()
    finally:
        await conn.close()
