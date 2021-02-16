from app import db
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    recipes = db.relationship('Recipe',backref='author',lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)   
        
class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    ingredients = db.Column(db.String())
    steps = db.Column(db.String())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, ingredients, steps,timestamp,user_id):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.timestamp = timestamp
        self.user_id = user_id

    def __repr__(self):
        return '<Recipes {}>'.format(self.id,self.name)