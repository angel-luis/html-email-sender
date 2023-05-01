import json
from pathlib import Path
import smtplib
from email.message import EmailMessage

# Load settings from JSON
with Path("./smtp_settings.json").open() as settings_json:
    settings = json.loads(settings_json.read())


def create_message():
    msg = EmailMessage()
    msg.set_content = "Hello world!"
    msg["Subject"] = f'The contents of {settings["subject"]}'
    msg["From"] = settings["from"]
    msg["To"] = settings["to"]
    return msg


msg_data = create_message()

with smtplib.SMTP(settings["smtp-server"]) as server:
    server.set_debuglevel(1)
    server.login(settings["smtp-user"], settings["smtp-password"])
    server.send_message(msg_data)
