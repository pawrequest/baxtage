from fastapi import Body, Depends
from loguru import logger
from sqlmodel import SQLModel, Session, select

from baxtage.back.db import get_session
from baxtage.back.routes_depends import db_model_from_path, response_model_from_path
from baxtage.models.people import ArtistBase, CrewBase, PersonBase
from baxtage.models.people_db import ArtistRole, Person


def merge_artist(
        artist: ArtistBase,
        session: Session,
        person_id: int | None = None,
        person: Person | None = None,
) -> ArtistRole:
    stmt = select(ArtistRole).where(ArtistRole.name == artist.name)
    if existing := session.exec(stmt).first():
        logger.debug(f'Existing: {existing=}')
        return existing

    person = parse_person(artist, session, person, person_id)

    new_artist = ArtistRole.model_validate(artist, from_attributes=True)
    new_artist.person = person

    session.add(new_artist)
    session.commit()
    session.refresh(new_artist)
    return new_artist


def check_name_exists[T: SQLModel](
        data: ArtistBase | CrewBase = Body(...),
        session: Session = Depends(get_session),
        db_model_type: type[T] = Depends(db_model_from_path),
) -> T:
    stmt = select(db_model_type).where(db_model_type.name == data.name)
    if existing := session.exec(stmt).first():
        logger.debug(f'Found Existing {db_model_type.__name__}: {existing=}')
        return existing


def merge_named[T: SQLModel](
        data: ArtistBase | CrewBase = Body(...),
        person_id: int | None = None,
        person: Person | None = None,
        session: Session = Depends(get_session),
        db_model_type: type[T] = Depends(db_model_from_path),
) -> T:
    if existing := check_name_exists():
        return existing

    person = parse_person(data, session, person, person_id)

    new_inst = db_model_type.model_validate(data, from_attributes=True)
    new_inst.person = person

    session.add(new_inst)
    session.commit()
    session.refresh(new_inst)
    return new_inst


def import_named[T: SQLModel](
        added: SQLModel = Depends(merge_named),
        response_class: type[T] = Depends(response_model_from_path),
) -> T:
    resp = response_class(added)
    return resp


def parse_person(named, session, person: Person | None = None, person_id: int | None = None):
    if not hasattr(named, 'name'):
        raise ValueError(f'Named object {named} has no name attribute')
    name = named.person_name if hasattr(named, 'person_name') else named.name

    if person:
        if person_id:
            raise ValueError('Only one of person_id or person should be provided')
        logger.debug(f'Passed: {person=}')
    elif person_id:
        person = session.get(Person, person_id)
        logger.debug(f'From id: {person=}')
    else:
        stmt = select(Person).where(Person.name == name)
        person = session.exec(stmt).first()
        logger.debug(f'From artist person_name: {person=}')

    if not isinstance(person, Person):
        person_ = PersonBase(name=named.person_name)
        person = Person.model_validate(person_, from_attributes=True)
        logger.debug(f'Created: {person=}')

    return person

def get_person(named, session, person: Person | None = None, person_id: int | None = None):
    if not hasattr(named, 'name'):
        raise ValueError(f'Named object {named} has no name attribute')
    name = named.person_name if hasattr(named, 'person_name') else named.name

    if person:
        if person_id:
            raise ValueError('Only one of person_id or person should be provided')
        logger.debug(f'Passed: {person=}')
    elif person_id:
        person = session.get(Person, person_id)
        logger.debug(f'From id: {person=}')
    else:
        stmt = select(Person).where(Person.name == name)
        person = session.exec(stmt).first()
        logger.debug(f'From artist person_name: {person=}')

    if not isinstance(person, Person):
        person_ = PersonBase(name=named.person_name)
        person = Person.model_validate(person_, from_attributes=True)
        logger.debug(f'Created: {person=}')

    return person


def new_person(person: PersonBase):
    ...
