from datetime import datetime, timezone
from app import db

class Estate(db.Model):
    __tablename__ = 'estates'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    courts = db.relationship('Court', backref='estate', lazy=True, cascade="all, delete-orphan")
    checkpoints = db.relationship('Checkpoint', backref='estate', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Estate {self.name}>"
