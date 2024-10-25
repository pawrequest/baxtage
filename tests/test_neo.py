import pytest
from loguru import logger

from baxtage.neo.n4j import Neo4jConnection
from baxtage.neo.neo_pyd import PersonNode
from baxtage.neo.queries import create_node


@pytest.fixture
def neo():
    uri = 'bolt://127.0.0.1:7687'
    pwd = 'Y2ws*$WUQFWo1^9jT0^NGT$O&*J7f'
    with Neo4jConnection(uri=uri, user="paw", pwd=pwd) as conn:
        yield conn


def test_neo(neo):
    assert neo.connected() is None


def test_q_manager(neo):
    q = create_node(label="Person", props={"name": "John"})
    res = neo.query(q)
    assert res is not None
    print(res)


@pytest.fixture(scope="module")
def person():
    n = PersonNode(name="John")
    res = n.model_validate(n)
    return res


def test_pyd_node(person):
    assert person.props_str() == '{ name: "John" }'
    assert person.name == "John"


def test_add_pyd_node(neo, person):
    q = person.create_q()
    logger.debug(q)
    res = neo.query(q)
    assert res is not None
    logger.debug(res)


def test_delete_pyd_node(neo, person):
    q = person.delete_q()
    logger.debug(q)
    res = neo.query(q)
    assert res is not None
    logger.debug(res)