from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login.utils import current_user, logout_user
from flask_login import login_user

from project.models import db, User
from project.auth import authorize
from project.forms import LoginForm

admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates'
)


@admin_bp.route('')
@authorize
def home():
    return 'this is admin home'


@admin_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('admin.home'))
        return render_template('register.html')

    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        new_user = User(email, password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('admin.login'))


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # POST request
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user is None or user.password != password:
            flash(('Email or password is wrong!'))
            return redirect(url_for('admin.login'))

        login_user(user)
        return redirect(url_for('admin.home'))

    # Get request
    if current_user.is_authenticated:
        return redirect(url_for('admin.home'))

    return render_template('login.html', form=form)


@admin_bp.route('/private', methods=['GET'])
@authorize
def private():
    return f"your pass {current_user.email}"


@admin_bp.route('/logout', methods=['GET'])
@authorize
def logout():
    logout_user()
    return redirect(url_for('admin.login'))
