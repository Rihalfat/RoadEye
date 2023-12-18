from live import predict_accident
from send_email import send_email_w_attachment

# Predicting Accident
predict_accident("s3://seniorwatertub/1.avi")

# Send email
to = "xxxxx@gmail.com"
subject = "There has been an accident"
body = """Hello, this is an automated message
\n The clip attached below shows that, there has been an accident and has been reported to you.
"""
filename = "s3://seniorwatertub/1.avi"

#calling the email function
send_email_w_attachment(to, subject, body, filename)