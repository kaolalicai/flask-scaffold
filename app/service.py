from flask import jsonify


class Service(object):
    @staticmethod
    def test(test_text):
        return jsonify({'test': test_text})
