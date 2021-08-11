from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
