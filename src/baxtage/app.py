from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from baxtage.back.db import create_db
from baxtage.back.routes_api import router as json_router
from baxtage.back.routes import router as html_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        create_db()
        logger.info('tables created')
        yield
    finally:
        ...


app = FastAPI(lifespan=lifespan)
app.include_router(json_router, prefix='/api')
app.include_router(html_router)


@app.get('/ping', response_model=str)
async def ping() -> str:
    return 'pong'
