from datetime import datetime

import pytest
from neontology import init_neontology

from baxtage.neo.models.people import ActNode, PersonNode, PlaysInRel
from baxtage.neo.models.rels import ActInShowRel
from baxtage.neo.models.show import EventNode, ShowAtVenueRel, ShowNode, VenueAtEventRel, VenueNode

EVENT_START = datetime(2022, 1, 1)
EVENT_END = datetime(2022, 1, 2)
SHOW_START = datetime(2022, 1, 1, 12)
SHOW_END = datetime(2022, 1, 1, 13)


@pytest.fixture
def neon():
    init_neontology()


@pytest.fixture(scope="module")
def person():
    return PersonNode(name="John")


@pytest.fixture(scope="module")
def act():
    return ActNode(name="A Band")


@pytest.fixture(scope="module")
def event():
    return EventNode(name='A Festival', start=EVENT_START, end=EVENT_END)


@pytest.fixture(scope="module")
def venue():
    return VenueNode(name='Main Stage')


@pytest.fixture(scope="module")
def show():
    return ShowNode(start=SHOW_START, end=SHOW_END, name='A Band at A Venue')


def test_show(person, neon, event, venue, show, act):
    event.merge()
    person.merge()
    act.merge()
    venue.merge()
    show.merge()

    pers_in_act = PlaysInRel(source=person, target=act)
    pers_in_act.merge()

    act_in_show = ActInShowRel(source=act, target=show)
    act_in_show.merge()

    show_at_venue = ShowAtVenueRel(source=show, target=venue)
    show_at_venue.merge()

    venue_at_event = VenueAtEventRel(source=venue, target=event)
    venue_at_event.merge()
