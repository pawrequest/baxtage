from typing import ClassVar

from neontology import BaseRelationship

from baxtage.neo.models.people import ActNode
from baxtage.neo.models.show import ShowNode


class ActInShowRel(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "ActIn"

    source: ActNode
    target: ShowNode


class ShowHasActRel(BaseRelationship):
    __relationshiptype__ = "ShowHas"

    source: ShowNode
    target: ActNode
