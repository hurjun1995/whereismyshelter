from marshmallow import fields, Schema
import datetime
from . import db

class AccountModel(db.Model):
    """
    Account Model
    """

    # table name
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)