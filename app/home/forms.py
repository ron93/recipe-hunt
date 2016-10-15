from wtforms import Form,StringField

class Add_recipe():
    name = StringField('name')
    ingredients=StringField('ingredients')
    steps= StringField('steps')