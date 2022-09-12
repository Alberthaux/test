from flask import Flask
from flask_bootstrap import Bootstrap5
import os
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key'
    )
app.config['SECRET_KEY'] = '10a42d96348a2d28b325ac86'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)
from market import routes
from market import util

