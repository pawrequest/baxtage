from typing import Annotated

from pydantic import BeforeValidator

from baxtage.models.equipment import Instrument
from baxtage.models.people import ArtistBase, PersonBase

DUMPED_D = Annotated[dict, BeforeValidator(lambda x: x.model_dump())]
LIST_STRS = Annotated[list[str], BeforeValidator(lambda x: [str(i) for i in x])]


class ArtistResponse(ArtistBase):
    instruments: list[Instrument]
    person_id: int
    # acts: list[dict]


class PersonResponse(PersonBase):
    id: int
    artist_roles: LIST_STRS
