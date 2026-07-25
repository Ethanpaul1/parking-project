# Import the shared db instance from your core app factory module
from app import db

# Expose the User model so it is visible to the application factory context
from models.user import User


# Placeholder comments: As you and your friend create individual files,
# you will import them here so Flask-Migrate knows they exist.
# Example:
# from models.user import User
# from models.vehicle import Vehicle
