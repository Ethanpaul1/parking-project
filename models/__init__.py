# Import the shared db instance from your core app factory module
from app import db

# Register all models here chronologically
from models.user import User
from models.estate import Estate
from models.court import Court
from models.checkpoint import Checkpoint
from models.resident import Resident
from models.visitor import Visitor
from models.vehicle import Vehicle



# Placeholder comments: As you and your friend create individual files,
# you will import them here so Flask-Migrate knows they exist.
# Example:
# from models.user import User
# from models.vehicle import Vehicle
