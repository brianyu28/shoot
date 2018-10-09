import datetime
import os
import pytz
import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

from models import *

def send(name, position, time):

    message = format_msg(name, position, time)
    server = mail_server()
    msg = MIMEText(message, "html")
    msg["Subject"] = f"Shoot Meeting with {name}"
    msg["From"] = formataddr(("Shoot Adviser Meetings", "utf-8"), "bot@thecrimson.com")
    msg["To"] = "brian.yu@thecrimson.com"
    server.send_message(msg)

def format_msg(name, position, time):
    """Formats message."""

    contents = "Hi Brian,<br/><br/>"
    contents += "Someone has signed up for a Shoot meeting with you. "
    contents += "<ul>"

    contents += f"<li>Name: <b>{name}</b></li>"
    contents += f"<li>Position: <b>{position}</b></li>"
    contents += f"<li>Time: <b>{time}</b></li>"

    contents += "</ul>"
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
        server.login("bot@thecrimson.com", os.environ.get("BOT_PASSWORD"))
    except Exception:
        return None
    return server

if __name__ == "__main__":
    main()
