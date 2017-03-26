from flask_sqlalchemy import SQLAlchemy
from afterhacks import db


class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


    def __init__(self, username, email):
        self.username = username
        self.email = email




    def __repr__(self):
        return '<User %r>' % self.username


    @classmethod
    def get_by_id(self, id):

    	if id 


    def 