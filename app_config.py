from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 相关config
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_SALT'] = 'super-secret-salt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_BINDS'] = {
    'users': 'sqlite:///users.db',
    'business': 'sqlite:///tasks.db'
}

db = SQLAlchemy(app)
