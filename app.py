from flask_migrate import Migrate
from project import app
from project.models import db


migrate = Migrate(app, db)
