from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="../templates", static_url_path='', static_folder='../web')

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#installation
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:secret@localhost:30300/test?charset=utf8mb4'
db = SQLAlchemy(app)
