import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

import email_config as ec

def send_email_w_attachment(to, subject, body, filename):
    message = MIMEMultipart()

    message['From'] = Header(ec.user)
    message['To'] = Header(to)
    message['Subject'] = Header(subject)

    message.attach(MIMEText(body, 'plain', 'utf-8'))

    att_name = os.path.basename(filename)
    _f = open(filename, 'rb')
    att = MIMEApplication(_f.read(), _subtype="avi")
    _f.close()
    att.add_header('Content-Disposition', 'attachment', filename=att_name)
    message.attach(att)

    server = smtplib.SMTP_SSL(ec.host, ec.port)
    server.login(ec.user, ec.gmail_pass)

    server.sendmail(ec.user, to, message.as_string())
    server.quit()