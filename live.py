from ultralytics import YOLO
model = YOLO("C:\Live Feed\Accident-Detection-Model-master\yolov8n.pt")
model.predict(source="0", show=True, conf=0.25, save=True)

# only if accident happens (0.7 accuracy at least)
# save the vid to drive/any cloud
# extract the vid and send using smtp (email.py)