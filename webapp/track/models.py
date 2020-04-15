from datetime import datetime

from webapp import db


class Track(db.Model):
    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.String(250))
    raw_gpx = db.Column(db.Text())

    def __repr__(self):
        return '<Track {}>'.format(self.title)
