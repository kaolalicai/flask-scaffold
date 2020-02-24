import pytest
from app import create_app


@pytest.fixture
def test_app(request):
    app = create_app(environment='test')
    client = app.test_client()

    return client
