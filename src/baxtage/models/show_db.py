from sqlmodel import Field, Relationship, SQLModel

from baxtage.models.links_db import ActShowLink
from baxtage.models.show import EventBase, ShowBase, VenueBase


class Event(EventBase, SQLModel, table=True):
    """ eg a festival, or multi-stage venue
    name: constr(max_length=50)
    start: datetime
    end: datetime
    """
    id: int | None = Field(default=None, primary_key=True)

    venues: list['Venue'] = Relationship(back_populates="event")


class Venue(VenueBase, SQLModel, table=True):
    """ eg a stage, room, or area within an event"""
    id: int | None = Field(default=None, primary_key=True)

    event_id: int | None = Field(default=None, foreign_key="event.id")
    event: Event = Relationship(back_populates="venues")

    def __str__(self) -> str:
        return f'{self.name} at {self.event.name}'

    shows: list['Show'] = Relationship(back_populates="venue")


class Show(ShowBase, SQLModel, table=True):
    """ eg a single act or set
    on_stage: datetime
    start: datetime | None = None
    end: datetime | None = None
    off_stage: datetime
    """
    id: int | None = Field(default=None, primary_key=True)

    venue_id: int | None = Field(default=None, foreign_key="venue.id")
    venue: Venue = Relationship(back_populates="shows")

    acts: list['Act'] = Relationship(back_populates="shows", link_model=ActShowLink)
