from functools import wraps
from flask import flash, redirect, url_for
from flask_login import LoginManager, current_user
from .models import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


def authorize(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if current_user.is_authenticated:
            return f(*args, **kwargs)
        else:
            flash("You must login to use it!")
            return redirect(url_for('admin.login'))
    return decorated_func
