import ffmpeg

from ultralytics import YOLO
model = YOLO("C:\Live Feed\Accident-Detection-Model-master\yolov8n.pt")
model.predict(source="0", show=True, conf=0.25, save=True)


# only if accident happens (0.7 accuracy at least)
# save the vid to drive/any cloud
# extract the vid and send using smtp (email.py)
# hi 


# to = "mohdrihal.mr@gmail.com"
# subject = "An example email"
# body = "Hi, This email is an example of how to send emails in Python"
# filename = "0.avi"

# send_email_w_attachment(to, subject, body, filename)