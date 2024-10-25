from pydantic import BaseModel, model_validator

from baxtage.models.people import PersonBase


class PydNode(BaseModel):
    label: str | None = None

    @model_validator(mode='after')
    def val_label(self):
        if self.label is None:
            self.label = self.__class__.__name__
        return self

    def props_str(self):
        return f"{{ {', '.join([f'{k}: "{v}"' for k, v in self.model_dump().items() if v and k != 'label'])} }}"

    def create_q(self):
        return f"CREATE (n:{self.label} {self.props_str()}) RETURN n"

    def merge_q(self):
        return f"MERGE (n:{self.label} {self.props_str()}) RETURN n"

    def read_q(self):
        return f"MATCH (n:{self.label} {self.props_str()}) RETURN n"

    def delete_q(self):
        return f"DELETE (n:{self.label} {self.props_str()}) RETURN n"

    def patch_q(self):
        return f"UPDATE (n:{self.label} {self.props_str()}) RETURN n"


class PersonNode(PydNode, PersonBase):
    pass
