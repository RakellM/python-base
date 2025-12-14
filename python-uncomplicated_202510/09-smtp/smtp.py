#!/usr/bin/env python3
"""Exemples: email sending"""

import smtplib

SERVER = "localhost"
PORT = 8025


FROM = "raquelsmarques@gmail.com"
TO = ["destino@server.com", "outro@server.com"]
SUBJECT = "My email via Python"
TEXT = """\
This is my email sending using Python!
<b>Olá Mundo!</b>
"""

# SMTP
message = f"""\
From: {FROM}
To: {",".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
