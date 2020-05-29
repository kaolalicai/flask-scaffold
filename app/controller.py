"""controller"""
from flask import request
from schema import Schema
from app.service import Service


class Controller(object):

    @classmethod
    def test(cls) -> str:
        data = request.get_json()
        schema = {'test': str}
        data = Schema(schema).validate(data)
        return Service.test(data['test'])
