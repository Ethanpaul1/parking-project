from marshmallow import fields, validate
from app import ma
from models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True  # Automatically instantiates a database object on success
        include_fk = True     # Includes structural foreign keys like checkpoint_id

    # Explicit application layer constraints
    full_name = fields.String(required=True, validate=validate.Length(min=3, max=100))
    email = fields.Email(required=True)
    phone = fields.String(required=True, validate=validate.Length(min=5, max=20))
    role = fields.String(validate=validate.OneOf(['admin', 'operator']))
