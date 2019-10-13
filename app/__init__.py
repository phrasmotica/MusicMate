from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# create app and load config
app = Flask(__name__)
app.config.from_object(Config)

# create DB engine and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
