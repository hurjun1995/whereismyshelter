from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from marshmallow import fields, Schema

# initialize our db
db = SQLAlchemy()
bcrypt = Bcrypt()

from .accountModel import AccountModel, AccountSchema
from .shelterModel import ShelterModel, ShelterSchema
from .inHeadCountModel import InHeadCountModel, InHeadCountSchema
from .outHeadCountsModel import OutCountModel, OutCountSchema
from .ageModel import AgeModel, AgeSchema
from .genderModel import GenderModel, GenderSchema

# account relationship
AccountModel.shelter_id = db.Column(db.Integer, db.ForeignKey('shelters.id'))
AccountModel.shelter = db.relationship('ShelterModel', back_populates="shelters")
AccountSchema.shelter = fields.Nested(ShelterSchema)

# shelter relationship
ShelterModel.inHeadCounts = db.relationship('InHeadCountModel', back_populates="shelters")
ShelterSchema.inHeadCounts = fields.Nested(InHeadCountSchema, many=True)
ShelterModel.out_count = db.relationship('HeadCountModel', backref='shelters')
ShelterSchema.out_count = fields.Nested(OutCountSchema, many=True)

# age relationship
AgeModel.inHeadCount = db.relationship('InHeadCountModel', back_populates="ages")
AgeSchema.inHeadCount = fields.Nested(InHeadCountSchema)

# gender relationship
GenderModel.inHeadCount = db.relationship('InHeadCountModel', back_populates="genders")
GenderSchema.inHeadCount = fields.Nested(InHeadCountSchema)

# inHeadCount relationship
InHeadCountModel.shelter_id = db.Column(db.Integer, db.ForeignKey('shelters.id'), nullable=False)
InHeadCountModel.shelter = db.relationship('ShelterModel', back_populates="inHeadCount")
InHeadCountModel.age_id = db.Column(db.Integer, db.ForeignKey('ages.id'), nullable=False)
InHeadCountModel.age = db.relationship('AgeModel', back_populates="inHeadCount")
InHeadCountModel.gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'), nullable=False)
InHeadCountModel.gender = db.relationship('GenderModel', back_populates="inHeadCount")
InHeadCountSchema.shelter_id = fields.Int(required=True)
InHeadCountSchema.shelter = fields.Nested(ShelterSchema)
InHeadCountSchema.age_id = fields.Int(required=True)
InHeadCountSchema.age = fields.Nested(AgeSchema)
InHeadCountSchema.gender_id = fields.Int(required=True)
InHeadCountSchema.gender = fields.Nested(GenderSchema)

# outHeadCount relationship
OutCountModel.shelter_id = db.Column(db.Integer, db.ForeignKey('shelters.id'), nullable=False)
OutCountSchema.shelter_id = fields.Int(required=True)
