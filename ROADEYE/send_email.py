# import time
# from datetime import date
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

# t = time.localtime()
# ct = time.strftime("%H:%M", t)
# today = date.today()
# d = today.strftime("%B %d, %Y")

# to = "mohdrihal.mr@gmail.com"
# subject = "Accident Notification"
# body = f"This email was sent by RoadEye at {ct} on {d}. \n An accident has been reported in the parking lot. \n Please take immediate action to address the situation. Please check details attached: \n"
# filename = "1.avi"

# send_email_w_attachment(to, subject, body, filename)