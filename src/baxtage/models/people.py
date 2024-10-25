# from __future__ import annotations

from pydantic import Field, constr, model_validator

from baxtage.models.equipment import Instrument
from baxtage.models.shared import BaxBase


class RoleBase(BaxBase):
    name: constr(max_length=50)

    def __str__(self):
        return self.name


class CrewBase(RoleBase):
    quals: list[str] = Field(default_factory=list)


class ArtistBase(RoleBase):
    instruments: list[Instrument] = Field(default_factory=list)
    person_name: str | None = None

    @model_validator(mode='after')
    def set_p_name(self):
        self.person_name = self.person_name or self.name
        return self


class PersonBase(BaxBase):
    name: constr(max_length=50)


class ActBase(BaxBase):
    name: constr(max_length=50)


class JobBase(BaxBase):
    name: constr(max_length=50)
