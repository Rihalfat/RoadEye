from ultralytics import YOLO

# model = YOLO("C:\Live Feed\Accident-Detection-Model-master\yolov8n.pt")
# model.predict(source="0", show=True, conf=0.25, save=True)

# def predict_accident():
#     model = YOLO("C:\Live Feed\Accident-Detection-Model-master\yolov8n.pt")
#     model.predict(source="0", show=True, conf=0.25, save=True)
import cv2


def predict_accident(filename):
    # Assuming YOLO is initialized inside the function
    model = YOLO("C:\Live Feed\Accident-Detection-Model-master\yolov8n.pt")

    # Start capturing video
    # Change the source if using a different camera or video file
    cap = cv2.VideoCapture(0)

    # Video resolution and frame rate
    width = 640
    height = 480
    fps = 8

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec (change as needed)
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error reading frame.")
            break

        # Perform prediction on the frame
        # model.predict(frame, conf=0.25, show=True, save=True)
        model.predict(frame, conf=0.25, show=True)
        out.write(frame)

        # Check for key press to stop the live feed (e.g., press 'q' to quit)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()


# Call the function to start the prediction
predict_accident('1.avi')

#only if accident happens (0.7 accuracy at least)
#send using smtp (email.py)
#hi

"""
    -------- CALL TO SEND EMAIL FUNCTION --------
"""
# to = "mohdrihal.mr@gmail.com"
# subject = "An example email"
# body = "Hi, This email is an example of how to send emails in Python"
# filename = "runs\detect\predict\0.avi"

# send_email_w_attachment(to, subject, body, filename)