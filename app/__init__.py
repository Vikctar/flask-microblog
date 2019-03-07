from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config
"""
This script creates the application object as an instance of class Flask
imported from the flask package. 
"""

app = Flask(__name__)

# Read and apply the config file.
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models