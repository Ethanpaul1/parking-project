from schemas.user_schema import UserSchema
from schemas.vehicle_schema import VehicleSchema
from schemas.parking_schema import ParkingRecordSchema, BlockingIncidentSchema

# Instantiate single-record and collection schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)

vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)

parking_record_schema = ParkingRecordSchema()
blocking_incident_schema = BlockingIncidentSchema()
