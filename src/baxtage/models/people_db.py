from typing import Literal

from sqlalchemy import Column, JSON
from sqlmodel import Field, Relationship, SQLModel
from pawdantic.pawsql import default_json_field

from baxtage.models.equipment import Instrument
from baxtage.models.links_db import ActArtistLink, ActShowLink
from baxtage.models.people import ActBase, ArtistBase, CrewBase, JobBase, PersonBase
from baxtage.models.show_db import Show

Roles = Literal['artist', 'crew']


class ArtistRole(ArtistBase, SQLModel, table=True):
    __tablename__ = 'artist'
    id: int | None = Field(default=None, primary_key=True)
    instruments: list[Instrument] = default_json_field(Instrument, default_factory=list)

    person_id: int = Field(None, foreign_key="person.id")
    person: 'Person' = Relationship(back_populates="artist_roles")
    person_name: str | None = None

    acts: list['Act'] = Relationship(back_populates="artists", link_model=ActArtistLink)


class CrewRole(CrewBase, SQLModel, table=True):
    __tablename__ = 'crew'
    id: int | None = Field(default=None, primary_key=True)
    quals: list[str] = Field(default_factory=list, sa_column=Column(JSON))

    person_id: int = Field(..., foreign_key="person.id")
    person: 'Person' = Relationship(back_populates="crew_roles")

    contact_for: list['Act'] = Relationship(back_populates="contact")
    jobs: list['Job'] = Relationship(back_populates="crew")

    # acts: list[ActBase] = Relationship(back_populates="performers")


class Person(PersonBase, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(..., index=True, unique=True)

    artist_roles: list[ArtistRole] = Relationship(back_populates="person")
    crew_roles: list[CrewRole] = Relationship(back_populates="person")


class Act(ActBase, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    contact_id: int | None = Field(default=None, foreign_key="crew.id")
    contact: 'CrewRole' = Relationship(back_populates="contact_for")

    shows: list['Show'] = Relationship(back_populates="acts", link_model=ActShowLink)
    artists: list[ArtistRole] = Relationship(back_populates="acts", link_model=ActArtistLink)


class Job(JobBase, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    crew_id: int | None = Field(default=None, foreign_key="crew.id")
    crew: CrewRole = Relationship(back_populates="jobs")

# class ModelResponse[T:type[SQLModel]](T):
#     id: int
#     ...
