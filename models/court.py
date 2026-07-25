from datetime import datetime, timezone
from app import db

class Court(db.Model):
    __tablename__ = 'courts'
    
    id = db.Column(db.Integer, primary_key=True)
    estate_id = db.Column(db.Integer, db.ForeignKey('estates.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    checkpoints = db.relationship('Checkpoint', backref='court', lazy=True)

    def __repr__(self):
        return f"<Court {self.name} - Estate ID: {self.estate_id}>"
