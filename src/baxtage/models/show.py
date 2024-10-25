# from __future__ import annotations
from datetime import datetime

from pydantic import constr

from baxtage.models.shared import BaxBase


class EventBase(BaxBase):
    """ eg a festival, or multi-stage venue"""
    name: constr(max_length=50)
    start: datetime
    end: datetime


class VenueBase(BaxBase):
    """ eg a stage, room, or area within an event"""
    name: constr(max_length=50)


class ShowBase(BaxBase):
    """ eg a single act or set"""
    on_stage: datetime
    start: datetime | None = None
    end: datetime | None = None
    off_stage: datetime
    # acts: list[ActBase] = Field(default_factory=list)
