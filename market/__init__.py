from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from market import routes
from market import models



