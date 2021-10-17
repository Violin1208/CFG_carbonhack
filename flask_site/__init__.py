from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'you-will-never-guess'
Bootstrap(app)

from flask_site import routes