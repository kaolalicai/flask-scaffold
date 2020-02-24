import pytest


@pytest.mark.usefixtures("testapp")
class TestURLs:
    def test_home(self, testapp):
        """
        test the home page
        """

        r = testapp.post('/log/write')
        print(r.__dict__)
        print(r.data)
        assert r.status_code == 200
