import pytest
from chatbotapp import app


@pytest.fixture(scope='module')
def test_client():
    """This method is used to initiate a testing client that will be used to in as an 
        interface for requests for tests.
    """

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client