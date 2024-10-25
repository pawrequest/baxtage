from starlette.testclient import TestClient

from baxtage.app import app


def get_test_session(test_session):
    return test_session


test_client = TestClient(app)

app.dependency_overrides = {
    'get_session': get_test_session
}


def test_test_client():
    with test_client as client:
        response = client.get('/ping')
        assert response.status_code == 200
        assert response.json() == 'pong'


def test_post_a_person(sample_person):
    with test_client as client:
        response = client.post('/api/person', json=sample_person.model_dump())
        assert response.status_code == 200
        person = response.json()
        assert person['name'] == sample_person.name
        artist = client.post('/api/artist', json={'name': 'Guitarist', 'person_id': person['id']})
        assert artist.status_code == 200


def test_post_an_artist(sample_artist):
    with test_client as client:
        response = client.post('/api/Artist', json=sample_artist.model_dump())
        assert response.status_code == 200
