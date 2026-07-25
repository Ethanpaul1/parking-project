from marshmallow import fields, validate
from app import ma
from models.parking import ParkingRecord, BlockingIncident

class ParkingRecordSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ParkingRecord
        load_instance = True
        include_fk = True

    status = fields.String(validate=validate.OneOf(['active', 'completed', 'blocked']))


class BlockingIncidentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BlockingIncident
        load_instance = True
        include_fk = True

    status = fields.String(validate=validate.OneOf(['reported', 'resolved']))
    description = fields.String(required=True, validate=validate.Length(min=5))
