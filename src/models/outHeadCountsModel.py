from marshmallow import fields, Schema
import datetime
from . import db


class OutCountModel(db.Model):
    """
    Account Model
    """

    # table name
    __tablename__ = 'outHeadCounts'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    shelter_id = db.Column(db.Integer, db.ForeignKey('shelter.id'), nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        :param data:
        """
        self.id = db.Column(db.Integer, primary_key=True)
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_outcount():
        return OutCountModel.query.all()

    def __repr__(self):
        return '<id {}>'.format(self.id)


class OutCountSchema(Schema):
    """
    Head Count Schema
    """
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    shelter_id = fields.Int(required=True)
