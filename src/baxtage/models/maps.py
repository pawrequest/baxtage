from dataclasses import dataclass
from typing import Literal

from baxtage.models.people import ArtistBase, PersonBase
from baxtage.models.people_db import Act, ArtistRole, CrewRole, Person
from baxtage.models.response import ArtistResponse, PersonResponse
from baxtage.models.show_db import Event, Show, Venue


@dataclass
class ModelMap:
    input_class: type
    db_class: type
    response_class: type


Category = Literal['artist', 'act', 'person', 'crew', 'show', 'venue', 'event']

MODEL_LOOKUP = {
    'artist': ModelMap(
        input_class=ArtistBase,
        db_class=ArtistRole,
        response_class=ArtistResponse,
    ),
    'person': ModelMap(
        input_class=PersonBase,
        db_class=Person,
        response_class=PersonResponse
    ),

}

ALL_TYPES = ArtistRole | Act | Person | CrewRole | Show | Venue | Event
