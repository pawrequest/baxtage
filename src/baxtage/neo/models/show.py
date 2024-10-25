from datetime import datetime
from typing import ClassVar

from neontology import BaseNode, BaseRelationship


class EventNode(BaseNode):
    __primarylabel__: ClassVar[str] = "Show"
    __primaryproperty__: ClassVar[str] = "name"

    name: str
    start: datetime
    end: datetime


class VenueNode(BaseNode):
    __primarylabel__: ClassVar[str] = "Venue"
    __primaryproperty__: ClassVar[str] = "name"

    name: str


class ShowNode(BaseNode):
    __primarylabel__: ClassVar[str] = "Show"
    __primaryproperty__: ClassVar[str] = "name"

    name: str

    on_stage: datetime | None = None
    start: datetime
    end: datetime
    off_stage: datetime | None = None


# Relationship

class VenueAtEventRel(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "VenueAt"

    source: VenueNode
    target: EventNode


class EventHasVenueRel(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "EventHas"

    source: EventNode
    target: VenueNode


class ShowAtVenueRel(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "ShowAt"

    source: ShowNode
    target: VenueNode


class VenueHasShowRel(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "VenueHas"

    source: VenueNode
    target: ShowNode
