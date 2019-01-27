from marshmallow import fields, Schema
from . import db


class GenderModel(db.Model):
    """
    Gender Model
    """

    # table name
    __tablename__ = 'genders'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(128), nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        :param data:
        """
        self.type = data.get('type')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_age():
        return GenderModel.query.all()

    @staticmethod
    def get_age_by_id(id):
        return GenderModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class GenderSchema(Schema):
    """
    InHeadCount Schema
    """
    id = fields.Int(dump_only=True)
    type = fields.String(required=True)
