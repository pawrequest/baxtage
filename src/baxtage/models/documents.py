from __future__ import annotations

from pydantic import BaseModel, Field, constr

from baxtage.models.equipment import Instrument


class TechSpec(BaseModel):
    instruments: list[Instrument] = Field(default_factory=list)
    notes: constr(max_length=500)
