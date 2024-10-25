from typing import Literal

from fastapi import APIRouter, Depends
from loguru import logger
from sqlmodel import SQLModel
from starlette.responses import JSONResponse

from baxtage.back.routes_depends import get_all_from_path, get_one_from_path_id, response_model_from_path
from baxtage.models.factory import merge_named

router = APIRouter()

Category = Literal['artist', 'act', 'person', 'crew', 'show', 'venue', 'event']


# @router.post('/artist', response_class=JSONResponse)
@router.post('/{category}', response_class=JSONResponse)
async def create_artist[T:SQLModel](
        added=Depends(merge_named),
        response_class: type[T] = Depends(response_model_from_path)
) -> T:
    # added = merge_artist(artist, session=session)
    resp = response_class(added)
    return resp


# @router.post('/artist', response_class=JSONResponse)
# async def create_artist(
#         artist: ArtistBase = Body(...),
#         session=Depends(get_session),
# ) -> ArtistResponse:
#     # added = merge_artist(artist, session=session)
#     added = merge_named(artist, session=session)
#     resp = ArtistResponse.model_validate(added, from_attributes=True)
#     return resp


@router.get('/{category}/{id}', response_class=JSONResponse)
async def get_by_id[T:SQLModel](
        record=Depends(get_one_from_path_id),
        response_class: [type[T]] = Depends(response_model_from_path)
) -> T:
    resp = response_class.model_validate(record, from_attributes=True)
    logger.debug(f'{record=}, {resp=}')
    return resp


@router.get('/{category}', response_class=JSONResponse)
async def get_all[T:SQLModel](
        records: list[SQLModel] = Depends(get_all_from_path),
        response_class: [type[T]] = Depends(response_model_from_path)
) -> dict[str, list[T]]:
    records = [response_class.model_validate(record, from_attributes=True) for record in records]
    return {'records': records}
