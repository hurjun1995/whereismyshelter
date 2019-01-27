from marshmallow import fields, Schema
import datetime
from . import db
from . import bcrypt


class AccountModel(db.Model):
    """
    Account Model
    """

    # table name
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        :param data:
        """
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.email = data.get('email')
        self.password = AccountModel.__generate_hash(data.get('password'))
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            if key == 'password':
                self.password = AccountModel.__generate_hash(item)
            setattr(self, key, item)
        self.modified_at = datetime.datetime
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def get_all_users():
        return AccountModel.query.all()

    @staticmethod
    def get_one_user(id):
        return AccountModel.query.get(id)

    @staticmethod
    def get_user_by_email(email):
        return AccountModel.query.get(email)

    @staticmethod
    def __generate_hash(password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

    def __repr__(self):
        return '<id {}>'.format(self.id)


class AccountSchema(Schema):
    """
    Account Schema
    """
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
