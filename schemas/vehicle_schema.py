from marshmallow import fields, validate, ValidationError, validates_schema
from app import ma
from models.vehicle import Vehicle

class VehicleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vehicle
        load_instance = True
        include_fk = True

    plate_number = fields.String(required=True, validate=validate.Length(min=3, max=20))
    brand = fields.String(validate=validate.Length(max=50))
    model = fields.String(validate=validate.Length(max=50))
    color = fields.String(validate=validate.Length(max=30))

    # Strict Application Layer Logic Validation Check
    @validates_schema
    def validate_polymorphic_ownership(self, data, **kwargs):
        resident_id = data.get('owner_resident_id')
        visitor_id = data.get('owner_visitor_id')

        # Scenario A: Payload attempts to assign both types of owners
        if resident_id and visitor_id:
            raise ValidationError("A vehicle cannot belong to both a Resident and a Visitor simultaneously.")
            
        # Scenario B: Payload provides neither owner assignment
        if not resident_id and not visitor_id:
            raise ValidationError("A vehicle must be assigned to either a Resident or a Visitor.")
