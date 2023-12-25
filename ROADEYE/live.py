from ultralytics import YOLO
import cv2

def predict_accident(filename):
    # Assuming YOLO is initialized inside the function
    model = YOLO("D:\RoadEye\ROADEYE\yolov8n.pt")

    # Start capturing video
    cap = cv2.VideoCapture(0)

    # Video resolution and frame rate
    width = 640
    height = 480
    fps = 8

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error reading frame.")
            break

        model.predict(frame, conf=0.25, show=True)
        out.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()