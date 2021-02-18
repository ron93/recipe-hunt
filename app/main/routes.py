from app.main import main_bp 
from flask import render_template
from flask_login import login_required


@main_bp.route('/')
@main_bp.route('/index')
def index():
    recipes = [
            {'author':{'username': 'James'},
                    'name':'Tea',
            'ingredients':{1:'Hot water',2:'Tea leaves',3:'Sugar'},
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
    return render_template('main/index.html',title='Home',recipes=recipes)

@main_bp.route('/user/<username>')
@login_required
def user(username):
    #first_or_404 -> returns first result or 404 error if non is found
    user = user.query.filter_by(username=username).first_or_404()
    
    recipes = [
      
         {'author':user,
            'name':'Uji',
            'ingredients':{1:'Hot water',2:'flour',3:'Sugar'},
            'steps':{1:'Boil  water on stove',2:'stir as you add four',3:'Add sugar'}
      },
          {
            'author' : user,
            'name':'Ugali',
            'ingredients':{1:'Hot water',2:'Maize flour'},
            'steps':{1:'Boil  water on stove',2:'stir as you add four',3:'Add more flour till hardens'}
      }

    ]
    return render_template('main/user.html', user=user, recipes=recipes)