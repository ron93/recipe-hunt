from flask_wtf import Form
from wtforms import StringField

class add_recipe():

    name = StringField('')
    content = StringField('ingredients')
    steps = StringField('directions')

    




