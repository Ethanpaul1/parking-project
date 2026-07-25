from datetime import datetime, timezone
from app import db

class CheckpointLog(db.Model):
    __tablename__ = 'checkpoint_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    checkpoint_id = db.Column(db.Integer, db.ForeignKey('checkpoints.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    verified_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    action_type = db.Column(db.String(20), nullable=False)  # 'entry', 'exit'
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self):
        return f"<CheckpointLog ID: {self.id} - Action: {self.action_type}>"


class MovementHistory(db.Model):
    __tablename__ = 'movement_history'
    
    id = db.Column(db.Integer, primary_key=True)
    # Intentionally flat denormalized tracker parameters to power lightning fast dashboard queries
    plate_number = db.Column(db.String(20), index=True, nullable=False)
    action = db.Column(db.String(50), nullable=False)  # 'entered_main_gate', 'parked', 'exited_court'
    details = db.Column(db.String(255), nullable=True)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self):
        return f"<MovementHistory {self.plate_number} - Action: {self.action}>"
