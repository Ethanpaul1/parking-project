from datetime import datetime, timezone
from app import db

class Visitor(db.Model):
    __tablename__ = 'visitors'
    
    id = db.Column(db.Integer, primary_key=True)
    host_resident_id = db.Column(db.Integer, db.ForeignKey('residents.id'), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    vehicles = db.relationship('Vehicle', backref='visitor_owner', lazy=True)

    def __repr__(self):
        return f"<Visitor {self.full_name} - Host ID: {self.host_resident_id}>"
