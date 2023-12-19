from ultralytics import YOLO
import cv2
from send_email import send_email_w_attachment

def predict_accident(filename):
    # Assuming YOLO is initialized inside the function
    model = YOLO("D:\RoadEye\ROADEYE\yolov8n.pt")

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

        results = model.predict(frame, conf=0.25, show=True)
        out.write(frame)
        # print(results[0])
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

predict_accident('1.avi')

# from ultralytics import YOLO
# import cv2
# import boto3
# from send_email import send_email_w_attachment

# def upload_to_s3(local_file_path, s3_bucket, s3_key):
#     s3 = boto3.client('s3')
#     s3.upload_file(local_file_path, s3_bucket, s3_key)


# # def download_from_s3(s3_bucket, s3_key, local_file_path):
# #     s3 = boto3.client('s3')
# #     s3.download_file(s3_bucket, s3_key, local_file_path)


# def predict_accident(filename):
#     model = YOLO("D:\RoadEye\ROADEYE\yolov8n.pt")
    
#     # Start capturing video
#     cap = cv2.VideoCapture(0)

#     # Video resolution and frame rate
#     width = 640
#     height = 480
#     fps = 8

#     fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec
#     out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

#     while True:
#         ret, frame = cap.read()

#         if not ret:
#             print("Error reading frame.")
#             break

#         # results = model.predict(frame, conf=0.25, show=True)
#         model.predict(frame, conf=0.25, show=True)
#         out.write(frame)
#         # print(results[0])
#         key = cv2.waitKey(1)
#         if key == ord('q'):
#             break

#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()

#     # Upload the video to AWS S3
#     s3_bucket = 'seniorwatertub'
#     s3_key = '1.avi'
#     upload_to_s3('1.avi', s3_bucket, s3_key)


# Example usage
# predict_accident('s3://seniorwatertub/1.avi')


# only if accident happens

# to = "mohdrihal.mr@gmail.com"
# subject = "Accident Notification"
# body = f"This email was sent by RoadEye at {ct} on {d}. \n An accident has been reported in the parking lot. \n Please take immediate action to address the situation.
# Please check details attached: \n"
# filename = "1.avi"

# send_email_w_attachment(to, subject, body, filename)