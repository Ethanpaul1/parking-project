from datetime import datetime, timezone
from app import db

class Resident(db.Model):
    __tablename__ = 'residents'
    
    id = db.Column(db.Integer, primary_key=True)
    court_id = db.Column(db.Integer, db.ForeignKey('courts.id'), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    house_number = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    vehicles = db.relationship('Vehicle', backref='resident_owner', lazy=True)
    visitors = db.relationship('Visitor', backref='host', lazy=True)

    def __repr__(self):
        return f"<Resident {self.full_name} - House: {self.house_number}>"
