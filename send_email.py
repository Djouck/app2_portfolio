import smtplib, ssl

host = "smtp.gmail.com"
port = 465


username = "giulia.ruffini445@gmail.com"
password = "khppbeksdhzciiap"

receiver = "giulia.ruffini445@gmail.com"
context = ssl.create_default_context()
message = """\
Subject: Hi!
How are you?
Bye!
PS Questa e la precedente email sono state inviate tramite Python!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)