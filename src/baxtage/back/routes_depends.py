from fastapi import Body, Depends, Path
from loguru import logger
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from baxtage.back.db import get_session
from baxtage.models.maps import ALL_TYPES, Category, MODEL_LOOKUP


async def response_model_from_path(category: Category = Path(...)) -> type[ALL_TYPES]:
    return MODEL_LOOKUP.get(category.lower()).response_class


async def db_model_from_path(category: Category = Path(...)) -> type[ALL_TYPES]:
    return MODEL_LOOKUP.get(category.lower()).db_class


async def get_all_from_path(
        model_type: type[ALL_TYPES] = Depends(db_model_from_path),
        session: Session = Depends(get_session)
):
    return session.exec(select(model_type)).all()


async def get_people(
        session: Session = Depends(get_session)
):
    model_type = MODEL_LOOKUP.get('person').db_class
    return session.exec(select(model_type)).all()


async def get_one_from_path_id[T:ALL_TYPES](
        model_type: type[T] = Depends(db_model_from_path),
        id: int = Path(...),
        session: Session = Depends(get_session)
) -> T:
    return session.get(model_type, id)


async def post_one(
        record=Body(...),
        session: Session = Depends(get_session),
        model_type=Depends(db_model_from_path),
) -> ALL_TYPES:
    try:
        record = model_type.model_validate(record)
        session.add(record)
        session.commit()
        session.refresh(record)
    except ValidationError as e:
        logger.error(f'Validation error: {e}')
    except IntegrityError as e:
        session.rollback()
        logger.warning('Record already exists')
        stmt = select(model_type).where(model_type.name == record.name)
        record = session.exec(stmt).first()
    return record
