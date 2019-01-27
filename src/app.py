from flask import Flask, url_for, request

from .config import app_config
from .models import db, bcrypt, accountModel


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    bcrypt.init_app(app)
    db.init_app(app)

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Your first endpoint is workin'

    @app.route('/login', method=['POST'])
    def login():
        data = request.get_json() or {}
        user = accountModel.AccountModel.get_user_by_email(data['body']['email'])
        if user:
            return user
        else:
            return ''

    @app.route('/count/v1/out', method=['POST'])
    def count_out():

        data = request.get_json or {}
        return foo(data)

    @app.route('/count/', method=['GET'])
    def get_count():
        return foo(data)

    @app.route('/count/v1/in', method=['POST'])
    def count_in():
        data = request.get_json or {}
        return foo(data)

    @app.route('/register', method=['POST'])
    def register_shelter():
        data = request.get_json or {}
        return foo(data)

    return app
