from datetime import datetime
from extensions import db

class User(db.Model):
    __tablename__ = 'ports'
    id = db.Column(db.Integer, primary_key=True)
    portname = db.Column(db.String(100))
    state = db.Column(db.String(100))
    address = db.Column(db.String(200))
    portcity = db.Column(db.String(100))
    contact = db.Column(db.String(100))
    status = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    @property
    def data(self):
        return {
            'id': self.id,
            'portname': self.portname,
            'state': self.state,
            'address': self.address,
            'portcity': self.portcity,
            'contact': self.contact
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
