import pytest
from sqlmodel import SQLModel, Session, StaticPool, create_engine

from baxtage.models.people_db import Person




def test_mod(test_session):
    person = Person(name="John Doe")
    assert person
