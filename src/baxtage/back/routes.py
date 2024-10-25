from fastapi import APIRouter
from starlette.responses import HTMLResponse

router = APIRouter()

router.get('/artist/', response_class=HTMLResponse)


def artist():
    return 'artist'
