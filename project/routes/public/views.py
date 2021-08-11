from flask import Blueprint

public_bp = Blueprint(
    'public',
    __name__,
    template_folder='templates'
)


@public_bp.route('')
def home():
    return 'Public home'


@public_bp.route('/login')
def login():
    return "login"
