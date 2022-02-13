from app import db


class Dataset(db.Model):
    __tablename__ = 'datasets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    filename = db.Column(db.String(64), index=True, unique=True)
    filepath = db.Column(db.String(128), index=True, unique=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Dataset {}>'.format(self.name)
