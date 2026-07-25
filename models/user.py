from datetime import datetime, timezone
from app import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False, default='operator')  # MVP flat string role
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Temporarily nullable integer until the checkpoints table model is written
    checkpoint_id = db.Column(db.Integer, nullable=True)
    
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<User {self.email} - Role: {self.role}>"
