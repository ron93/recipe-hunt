from app import db
from sqlalchemy.dialects.postgresql import JSON


class Recipes(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    ingredients = db.Column(db.String())
    steps = db.Column(db.String())

    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def __repr__(self):
        return '<id {}>'.format(self.id)