from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '333ddd333'

from src import routes
