#!/usr/bin/env python3
"""Imprime a mensagem de um e-mail

NAO MANDE SPAM!!!
"""
__version__ = "0.2.2"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

import sys
import os
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de emails.")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) # emails.txt
templatepath = os.path.join(path, templatename) # email_tmpl.txt

 
with smtplib.SMTP(host="localhost", port=8025) as server:

    for line in open(filepath, encoding='utf-8'):
        name, email = line.split(",")

        text = (
            open(templatepath, encoding='utf-8').read()
            % { 
                "nome": name,
                "produto": "caneta",
                "texto": "Escrever muito bem",
                "link": "http//canetaslegais.com",
                "quantidade": 1,
                "preco": 50.5,
            }
        )

        from_ = "raquelsmarques@gmail.com"
        to_ = ", ".join([email])

        message = MIMEText(text)
        message['Subject'] = "Compre mais!"
        message['From'] = from_
        message['To'] = to_

        server.sendmail(from_, to_, message.as_string())

