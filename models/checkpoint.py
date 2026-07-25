from datetime import datetime, timezone
from app import db

class Checkpoint(db.Model):
    __tablename__ = 'checkpoints'
    
    id = db.Column(db.Integer, primary_key=True)
    estate_id = db.Column(db.Integer, db.ForeignKey('estates.id'), nullable=False)
    
    # Nullable because a 'main_gate' belongs to the whole estate, not one small court
    court_id = db.Column(db.Integer, db.ForeignKey('courts.id'), nullable=True) 
    
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False, default='sub_gate')  # 'main_gate' or 'sub_gate'
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Checkpoint {self.name} - Type: {self.type}>"
