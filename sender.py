import json
from pathlib import Path
import smtplib
from email.message import EmailMessage
from string import Template

# Load settings from JSON
with Path("./smtp_settings.json").open() as settings_json:
    settings = json.loads(settings_json.read())

# Create message content from HTML template
with open("./body.html") as html:
    # Modify here the template strings
    msg_content = Template(html.read()).substitute(name=settings["name"])


def create_message():
    msg = EmailMessage()
    msg.set_content(msg_content, "html")
    msg["Subject"] = settings["subject"]
    msg["From"] = settings["from"]
    msg["To"] = settings["to"]
    return msg


msg_data = create_message()

with smtplib.SMTP_SSL(settings["smtp-server"], 465) as server:
    print("Sending message...")
    server.login(settings["smtp-user"], settings["smtp-password"])
    server.send_message(msg_data)

print("Message sent!")
