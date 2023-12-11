import smtplib
import ssl
from email.message import EmailMessage

email_sender = 'mohammedrihal.mr@gmail.com'
password = 'tidx dvxw iqcb qnmn'
email_receivers = ['nawafnazeer@gmail.com','zinnferns@gmail.com', 'groverhriday12@gmail.com']

subject = 'WAASSAAPP'
body = """Hi, this was sent using python"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = ', '.join(email_receivers)
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_receivers, em.as_string())