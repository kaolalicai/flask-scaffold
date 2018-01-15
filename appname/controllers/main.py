from flask import Blueprint, jsonify, request, current_app
from .valid_schemas import home_schema


main = Blueprint('main', __name__)

"""
Flask request 对象文档 http://flask.pocoo.org/docs/0.12/api/#incoming-request-data
"""


@main.route('/', methods=["GET"])
def home():
    return jsonify({"code": 0, "data": "Hello World"})


@main.route('/raise_error', methods=["GET"])
def raise_error():
    raise Exception('error')


@main.route('/post', methods=["POST"])
def common_indicators():
    return jsonify({"code": 0, "data": "Hello World"})


@main.route('/log/write', methods=['GET'])
def write_log():
    current_app.logger.info('log success')
    return jsonify({"code": 0, "data": "Hello World"})
