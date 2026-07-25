from flask import Blueprint, request, jsonify, session
from app import db
from models.user import User
from schemas.user_schema import UserSchema

# 1. Instantiate the authentication Blueprint context
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

user_schema = UserSchema()

@auth_bp.route('/register', methods=['POST'])
def register():
    """Handles basic user account creations."""
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Missing input data"}), 400

    # Validate incoming structural formats through Marshmallow
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    # Ensure email uniqueness via a basic lookup query
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"error": "An account with this email already exists"}), 400

    # Construct the user model using standard parameters
    new_user = User(
        full_name=data['full_name'],
        email=data['email'],
        phone=data['phone'],
        password=data['password'],  # Saved as clear plain text
        role=data.get('role', 'operator'),
        checkpoint_id=data.get('checkpoint_id')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully", "user_id": new_user.id}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """Handles basic plain-text password comparison verification sessions."""
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Email and password are required"}), 400

    # Find user profile row context
    user = User.query.filter_by(email=data['email']).first()

    # Standard equality check matching introductory coursework parameters
    if not user or user.password != data['password']:
        return jsonify({"error": "Invalid email or password"}), 401

    # Initialize a clean, native Flask server cookie session tracker
    session['user_id'] = user.id
    session['user_role'] = user.role

    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "role": user.role
        }
    }), 200


@auth_bp.route('/logout', methods=['POST'])
def logout():
    """Clears active session tracks from client request tokens."""
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200
