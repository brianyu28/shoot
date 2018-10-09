import datetime
import os
import pytz
import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

from models import *

def send(name, position, time, email):

    message = format_msg(name, position, time, email)
    server = mail_server()
    msg = MIMEText(message, "html")
    msg["Subject"] = f"{name}'s Shoot Meeting with BPY"
    msg["From"] = formataddr(("Shoot Adviser Brian Yu", "utf-8"), "bot@thecrimson.com")
    msg["To"] = email
    msg["Cc"] = "brian.yu@thecrimson.com"
    server.send_message(msg)

def format_msg(name, position, time, email):
    """Formats message."""

    contents = f"Hi {name},<br/><br/>"
    contents += "Thanks for signing up to meet with me. The details of the meeting are below: "
    contents += "<ul>"

    contents += f"<li>Name: <b>{name}</b></li>"
    contents += f"<li>Email: <b>{email}</b></li>"
    contents += f"<li>Position: <b>{position}</b></li>"
    contents += f"<li>Time (15-minute slot): <b>{time}</b></li>"

    contents += "</ul>"
    contents += "I'll reach out again shortly to confirm a location. See you soon!<br/><br/>All the best,<br/>Brian"
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
