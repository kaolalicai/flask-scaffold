"""router"""
from flask import Blueprint
from app.controller import Controller

main = Blueprint('main', __name__)


def home():
    return 'Hello world!'


def raise_error():
    raise Exception('error')


# 主页, 测试是否有效
main.add_url_rule(rule='/', view_func=home, methods=["GET", "POST"])
main.add_url_rule(rule='/raise', view_func=raise_error, methods=["GET"])

# controller demo
main.add_url_rule(rule='/test', view_func=Controller.test, methods=["POST"])

