from flask import jsonify


class Service(object):
    @staticmethod
    def test(test_text: str) -> str:
        return jsonify({'test': test_text})
