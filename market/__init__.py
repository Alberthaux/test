from flask import Flask
from flask_bootstrap import Bootstrap5
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = '10a42d96348a2d28b325ac86'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)
from market import routes
from market import util

