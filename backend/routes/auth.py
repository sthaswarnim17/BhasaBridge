from flask import Blueprint
from controllers.auth_controller import register_user, login_user

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    return register_user()

@auth.route('/login', methods=['POST'])
def login():
    return login_user()


