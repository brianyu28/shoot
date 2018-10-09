import datetime
import os
import pytz
import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

from models import *

def send(name, position, time, location, email, phone):

    message = format_msg(name, position, time, location, email, phone)
    server = mail_server()
    msg = MIMEText(message, "html")
    msg["Subject"] = f"{name}'s Shoot Meeting with BPY"
    msg["From"] = formataddr(("Shoot Adviser Brian Yu", "utf-8"), "brian.yu@thecrimson.com")
    msg["To"] = email
    msg["Cc"] = "brian.yu@thecrimson.com"
    server.send_message(msg)

def format_msg(name, position, time, location, email, phone):
    """Formats message."""
    location = location or "TBD (I'll follow up shortly to set up a location.)"

    contents = f"Hi {name},<br/><br/>"
    contents += "Thanks for signing up to meet with me. The details of the meeting are below: "
    contents += "<ul>"

    contents += f"<li>Name: <b>{name}</b></li>"
    contents += f"<li>Position: <b>{position}</b></li>"
    contents += f"<li>Contact Info: <b>{email}</b>, <b>{phone}</b></li>"
    contents += f"<li>Time (15-minute slot): <b>{time}</b></li>"
    contents += f"<li>Location: <b>{location}</b></li>"

    contents += "</ul>"
    contents += "Feel free to reach out if you have any questions. See you soon!<br/><br/>All the best,<br/>Brian"
    return contents

def mail_server():
    """
    Configures SMTP server.
    """

    # Connect to server.
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    try:
        server.login("brian.yu@thecrimson.com", os.environ.get("BOT_PASSWORD"))
    except Exception:
        return None
    return server

if __name__ == "__main__":
    main()
