from flask import Flask, request

from . import payment


def create_app():
    app = Flask(__name__)
    app.register_blueprint(payment.bp)

    return app
