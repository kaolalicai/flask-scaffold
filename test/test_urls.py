import pytest


@pytest.mark.usefixtures("test_app")
class TestURLs:
    def test_home(self, test_app):
        """
        test the home page
        """
        text = b'{"test":"True"}\n'
        r = test_app.post(
            '/test',
            data=text,
            content_type='application/json'
        )
        assert r.status_code == 200
        assert r.data == text
