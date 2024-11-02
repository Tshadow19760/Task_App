
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'TYDX'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


db = SQLAlchemy(app)

with app.app_context():
    db.create_all()
    print("Database tables created.")

from routes import *


if __name__ == '__main__':
    app.run(debug=True)
