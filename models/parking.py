from datetime import datetime, timezone
from app import db

class ParkingSlot(db.Model):
    __tablename__ = 'parking_slots'
    
    id = db.Column(db.Integer, primary_key=True)
    court_id = db.Column(db.Integer, db.ForeignKey('courts.id'), nullable=False)
    slot_number = db.Column(db.String(20), nullable=False)
    is_occupied = db.Column(db.Boolean, default=False, nullable=False)
    location_description = db.Column(db.String(255), nullable=True) # Optional structural fallback

    # Relationship
    records = db.relationship('ParkingRecord', backref='slot', lazy=True)

    def __repr__(self):
        return f"<ParkingSlot {self.slot_number} - Court ID: {self.court_id}>"


class ParkingRecord(db.Model):
    __tablename__ = 'parking_records'
    
    id = db.Column(db.Integer, primary_key=True)
    parking_slot_id = db.Column(db.Integer, db.ForeignKey('parking_slots.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    
    start_time = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(30), default='active', nullable=False)  # 'active', 'completed', 'blocked'

    # Relationships
    incidents = db.relationship('BlockingIncident', backref='record', lazy=True)

    def __repr__(self):
        return f"<ParkingRecord ID: {self.id} - Vehicle ID: {self.vehicle_id} - Status: {self.status}>"


class BlockingIncident(db.Model):
    __tablename__ = 'blocking_incidents'
    
    id = db.Column(db.Integer, primary_key=True)
    parking_record_id = db.Column(db.Integer, db.ForeignKey('parking_records.id'), nullable=False)
    reporter_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(30), default='resolved', nullable=False)  # 'reported', 'resolved'
    resolved_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self):
        return f"<BlockingIncident ID: {self.id} - Record ID: {self.parking_record_id}>"
