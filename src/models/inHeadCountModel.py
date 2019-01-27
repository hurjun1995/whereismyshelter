from marshmallow import fields, Schema
import datetime
from . import db

class InHeadCountModel(db.Model):
    """
    Account Model
    """

    # table name
    __tablename__ = 'inHeadCounts'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        :param data:
        """
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()
        self.shelter_id = data.get('shelter_id')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_inHeadCounts():
        return InHeadCountModel.query.all()

    @staticmethod
    def get_inHeadCount_by_id(id):
        return InHeadCountModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class InHeadCountSchema(Schema):
    """
    InHeadCount Schema
    """
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
