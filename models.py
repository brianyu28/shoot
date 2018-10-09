import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
uri = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Appointment(db.Model):
    __tablename__ = "gratitudes"
    id = db.Column(db.BigInteger, primary_key=True, nullable=False, autoincrement=True)
    date = db.Column(db.String(length=256))
    time = db.Column(db.String(length=256))
    name = db.Column(db.String(length=256))
    filled = db.Column(db.Boolean, default=False)

