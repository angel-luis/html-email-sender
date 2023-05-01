## Overview

Small project for learning Python. This script sends a _HTML_ template to an email via _SMTP_.

## Usage

Replace the dummy data inside **smtp_settings.json** with your server provider info and receiver.

Fill the **body.html** file with your custom _HTML_. You can use a template string, like `$name`, inside the body. If you want to add or modify the template strings, in **sender.py**, change the vars inside `msg_content` and also in **smtp_settings.json**.

```bash
python sender.py
```
