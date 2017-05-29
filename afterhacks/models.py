"""Contains models to build database tables"""
from afterhacks import db


class User(db.Model):
    """database model that manages User table"""
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


    def __init__(self, username, email):
        self.username = username
        self.email = email


    def __repr__(self):
        return '<User %r>' % self.username

    @classmethod
    def get_user_by_username(cls, username):
        """returns a user by username"""
        pass


    @classmethod
    def get_by_id(cls, user_id):
        """returns a user by id"""
        pass
