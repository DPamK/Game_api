from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 相关config
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_SALT'] = 'super-secret-salt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game_api.db'

db = SQLAlchemy(app)
