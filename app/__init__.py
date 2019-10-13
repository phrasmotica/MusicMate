from config import Config
from flask import Flask

# create app and load config
app = Flask(__name__)
app.config.from_object(Config)

from app import routes
