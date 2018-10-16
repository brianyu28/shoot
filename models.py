import datetime
import os
import pytz

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
uri = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Appointment(db.Model):
    __tablename__ = "appointments"
    id = db.Column(db.BigInteger, primary_key=True, nullable=False, autoincrement=True)
    time = db.Column(db.DateTime())
    location = db.Column(db.String(length=256), nullable=True)
    name = db.Column(db.String(length=256), nullable=True)
    position = db.Column(db.String(length=256), nullable=True)
    email = db.Column(db.String(length=256), nullable=True)
    category = db.Column(db.String(length=256), nullable=True)
    phone = db.Column(db.String(length=256), nullable=True)
    filled = db.Column(db.Boolean, default=False)
    visible = db.Column(db.Boolean, default=True)

    def add_slot(month, day, hour, minute, location=None):
        time = datetime.datetime(
            month=month, day=day, year=2018, hour=hour, minute=minute,
        )
        appt = Appointment(time=time, name=None, position=None, filled=False, location=location)
        db.session.add(appt)
        db.session.commit()

    def remove_slots(month, day):
        for appt in Appointment.query.all():
            if appt.time.month == month and appt.time.day == day:
                appt.visible = False
        db.session.commit()
