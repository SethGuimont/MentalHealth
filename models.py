from flask_sqlalchemy import SQLAlchemy

#Create extension
db = SQLAlchemy()


class User(db.Model):
    user = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

#https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#configure-the-extension