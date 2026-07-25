from datetime import datetime, timezone
from app import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Core unique indexed identifier
    plate_number = db.Column(db.String(20), unique=True, index=True, nullable=False)
    brand = db.Column(db.String(50), nullable=True)
    model = db.Column(db.String(50), nullable=True)
    color = db.Column(db.String(30), nullable=True)
    
    # Polymorphic Owner Tracks (Both nullable at DB level; application checks enforce exactly one)
    owner_resident_id = db.Column(db.Integer, db.ForeignKey('residents.id'), nullable=True)
    owner_visitor_id = db.Column(db.Integer, db.ForeignKey('visitors.id'), nullable=True)
    
    # Audit Logs: Who registered it and where
    registered_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    registered_at_checkpoint_id = db.Column(db.Integer, db.ForeignKey('checkpoints.id'), nullable=False)
    
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Vehicle {self.plate_number}>"
