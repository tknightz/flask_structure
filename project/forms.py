from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    email = StringField(
        "email", validators=[InputRequired(message="Email is required!")]
    )
    password = PasswordField(
        "password", validators=[InputRequired(message="Password is required!")]
    )
