from app.extensions import db
from datetime import datetime
import enum


class StatusEnum(enum.IntEnum):
    ACTIVE = "1"
    INACTIVE = "2"

class Team(db.Model):
    __tablename__ = "team_mdl" 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    profile = db.Column(db.String(100), nullable=True)
    file_path = db.Column(db.String(255), nullable=True)
    rem_addr = db.Column(db.String(50), nullable=True)
    status = db.Column(
        db.Integer, 
        nullable=False, 
        default=StatusEnum.ACTIVE, 
        comment="1: Active, 2: Inactive"
    ) 
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Team {self.id}>'   



