from app.auth import auth_bp

@auth_bp.route('/')
def index():
    return "Auth Blueprint"

@auth_bp.route('/lohin', methods=['GET', 'POST'])
def login():
    pass

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    pass
