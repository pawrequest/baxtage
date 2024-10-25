from typing import ClassVar

from neontology import BaseNode, BaseRelationship


class PersonNode(BaseNode):
    __primarylabel__: ClassVar[str] = "Person"
    __primaryproperty__: ClassVar[str] = "name"

    name: str


class ActNode(BaseNode):
    __primarylabel__: ClassVar[str] = "Act"
    __primaryproperty__: ClassVar[str] = "name"

    name: str


class JobNode(BaseNode):
    __primarylabel__: ClassVar[str] = "Job"
    __primaryproperty__: ClassVar[str] = "name"

    name: str


class PlaysInRel(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "PlaysIn"

    source: PersonNode
    target: ActNode


class DoesJobRel(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "DoesJob"

    source: PersonNode
    target: JobNode


class HasArtistRel(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HasArtist"

    source: ActNode
    target: PersonNode


class DoneByRel(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "DoneBy"

    source: JobNode
    target: PersonNode
