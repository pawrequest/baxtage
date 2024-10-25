from datetime import datetime

import pytest
from sqlalchemy import StaticPool, create_engine
from sqlmodel import SQLModel, Session

from baxtage.models.people_db import Person, ArtistRole, CrewRole, Act
from baxtage.models.show_db import Event, Venue, Show


@pytest.fixture(scope='function')
def engine_fxt():
    """
    Create an in-memory sqlite engine

    :return: sqlite engine
    """
    return create_engine('sqlite:///:memory:', connect_args={'check_same_thread': False}, poolclass=StaticPool)


@pytest.fixture(scope='session')
def test_session():
    """
    Create an in-memory sqlite session

    :return: sqlite session
    """
    # engine = engine_fxt
    engine = create_engine('sqlite:///:memory:', connect_args={'check_same_thread': False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture
def sample_person():
    person = Person(
        name="John Doe"
    )
    return person


@pytest.fixture
def sample_artist(sample_person):
    artist = ArtistRole(
        name="Guitarist",
        person=sample_person,
    )
    return artist


@pytest.fixture
def sample_crew(sample_person):
    crew = CrewRole(
        name="Sound Engineer",
        person=sample_person
    )
    return crew


@pytest.fixture
def sample_act(sample_artist, sample_crew):
    act = Act(
        name="Rock Band",
        contact=sample_crew,
        artists=[sample_artist]
    )
    return act


@pytest.fixture
def sample_event():
    event = Event(
        name="Music Festival",
        start=datetime(2024, 7, 1),
        end=datetime(2024, 7, 3)
    )
    return event


@pytest.fixture
def sample_venue(sample_event):
    venue = Venue(
        name="Main Stage",
        event=sample_event
    )
    return venue


@pytest.fixture
def sample_show(sample_event, sample_venue, sample_act):
    show = Show(
        on_stage=datetime(2024, 7, 2, 18, 0),
        off_stage=datetime(2024, 7, 2, 20, 0),
        venue=sample_venue
    )
    show.acts.append(sample_act)
    return show
