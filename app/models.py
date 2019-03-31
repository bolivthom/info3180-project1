from . import db


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(80), nullable=False)
    photo = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, first_name, last_name, email, gender, location, biography,  photo):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.location = location
        self.biography = biography
        self.photo = photo

    def __repr__(self):
        return '<User %r %r (%r)>' % (
            self.first_name,
            self.last_name,
            self.email
        )
