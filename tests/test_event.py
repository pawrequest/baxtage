from datetime import datetime

from baxtage.models.people_db import ArtistRole, Person
from conftest import sample_act, sample_crew, sample_event, sample_show, sample_venue


def test_sample_act(test_session, sample_act, sample_crew):
    test_session.add(sample_act)
    test_session.commit()

    assert sample_act.name == "Rock Band"
    assert sample_act.contact_id == sample_crew.id
    assert len(sample_act.artists) == 1
    assert sample_act.artists[0].name == "Guitarist"
    assert sample_act.artists[0].person.name == "John Doe"


####################################


### Test Cases

def test_event_with_show(test_session, sample_event, sample_venue, sample_show):
    test_session.add(sample_show)
    test_session.commit()
    # Verify the event was created correctly
    assert sample_event.id is not None
    assert sample_event.name == "Music Festival"

    # Verify the venue was created correctly
    assert sample_venue.id is not None
    assert sample_venue.name == "Main Stage"

    # Verify the show was created correctly
    assert sample_show.id is not None
    assert sample_show.on_stage == datetime(2024, 7, 2, 18, 0)
    assert sample_show.off_stage == datetime(2024, 7, 2, 20, 0)

    # Verify relationships
    assert sample_show.venue_id == sample_venue.id
    assert sample_show.venue.name == "Main Stage"
    assert len(sample_show.acts) == 1


def test_new_artist(test_session):
    person = {'name': 'Holla'}
    person_ = Person(**person)
    artist = ArtistRole(name='Holla Live', person=person_)
    test_session.add(artist)
    test_session.commit()
    test_session.refresh(artist)
    assert artist.id
    assert artist.model_validate(artist)
