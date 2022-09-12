from flask import Flask
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY') or 'dev_key'
    )

from rucoh import routes
from rucoh import util

