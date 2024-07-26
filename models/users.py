from extensions import db

class User(db.Model):
    __tablename__ = 'ports'
    id = db.Column(db.Integer, primary_key=True)
    portname = db.Column(db.String(80), nullable=False, unique=True)
    state = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    portcity = db.Column(db.String(80), nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

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
