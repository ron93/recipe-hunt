from app.auth import auth_bp


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    pass

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    pass
