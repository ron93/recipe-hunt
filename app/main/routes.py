from app.main import main_bp 
from flask import render_template
from flask_login import login_required


@main_bp.route('/')
@login_required
def index():
    user = {'username': 'Ron'}
    recipes = [
            {'author':{'username': 'James'},
                    'name':'Tea',
            'ingredients':{1:'Hot water',2:'Tea leaves',2:'Sugar'},
            'steps':{1:'Add hot water to cup',2:'Add tea 1 bag and 2 spoons sugar',3:'stir till color is consistent'}
            },
              {'author':{'username': 'Mary'},
            'name':'Uji',
            'ingredients':{1:'Hot water',2:'flour',2:'Sugar'},
            'steps':{1:'Boil  water on stove',2:'stir as you add four',3:'Add sugar'}
            },
               {'author':{'username': 'James'},
            'name':'Toast',
            'ingredients':{1:'Bread',2:'Butter'},
            'steps':{1:'Add butter to pan, let it melt at low heat',2:'put slice of bread',3:'Turn after 3 mins',4:'serve while hot'}
            }
        ]
    return render_template('main/index.html',title='Home', user=user,recipes=recipes)
    