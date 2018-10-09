import os

from flask import Flask, render_template, request
from helpers import *
from models import *
from send import *

app.jinja_env.filters["format_time"] = format_time

@app.route("/")
def index():
    appointments = Appointment.query.order_by(Appointment.time).all()
    return render_template("index.html", appointments=appointments)

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    appt_id = data["id"]
    name = data["name"]
    email = data["email"]
    position = data["position"]
    time = data["time"]
    appt = Appointment.query.get(appt_id)
    if (not appt) or appt.filled:
        return "Failed", 400
    else:
        # Fill the appointment
        appt.filled = True
        appt.name = name
        appt.position = position
        appt.email = email
        db.session.commit()

        send(name, position, time, email)

        # Notify me
        return "Success", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
