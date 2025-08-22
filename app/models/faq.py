from app.extensions import db
from datetime import datetime
import enum

class StatusEnum(enum.IntEnum):
    ACTIVE = "1"
    INACTIVE = "2"

class FAQ(db.Model):
    __tablename__ = "faq_mdl"
    
    #  __seachbale__ = ['name','description']
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.Text(), nullable=True)
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
        return f'<FAQ {self.id}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "desc": self.desc,
            #"rem_addr": self.rem_addr,
            #"status": self.status,
           # "created": self.created.isoformat() if self.created else None,
            #"updated": self.updated.isoformat() if self.updated else None,
        }
    


    def json(self):
        return {'id': self.id,'title': self.title, 'desc': self.desc}




