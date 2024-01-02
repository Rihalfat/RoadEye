from live import predict_accident
from send_email import send_email_w_attachment
import time
from datetime import date

# Predicting Accident
predict_accident("1.avi")

t = time.localtime()
ct = time.strftime("%H:%M", t)
today = date.today()
d = today.strftime("%B %d, %Y")

# Send email
to = "muhdrihaal.mr@gmail.com"
subject = "Accident Notification"
body = f"This email was sent by RoadEye at {ct} on {d}. \n An accident has been reported in the parking lot. \n Please take immediate action to address the situation. Please check details attached: \n"
filename = "1.avi"

#calling the email function
send_email_w_attachment(to, subject, body, filename)