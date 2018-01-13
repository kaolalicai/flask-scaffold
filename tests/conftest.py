import pytest

from appname import create_app


@pytest.fixture
def testapp(request):
    app = create_app('appname.settings.TestConfig')
    client = app.test_client()

    return client
