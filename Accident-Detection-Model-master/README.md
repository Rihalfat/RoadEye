## Model Set-up
#### Preparing Custom dataset
- We have collected 1200+ images from different sources like YouTube, Google images, Kaggle.com etc.
- Then we annotated all of them individually on a tool called roboflow.
- During Annotation we marked the images with no accident as NULL and we drew a box on the site of accident on the images having an accident
- Then we divided the data set into train, val, test in the ratio of 8:1:1
- At the final step we downloaded the dataset in yolov8 format.                                                                                    
#### Using Google Collab
- We are using google colaboratory to code this model because google  collab uses gpu which is faster than local environments.
- You can use Jupyter notebooks, which let you blend code, text, and visualisations in a single document, to write and run Python code using Google Colab.
- Users can run individual code cells in Jupyter Notebooks and quickly view the results, which is helpful for experimenting and debugging. Additionally, they enable the development of visualisations that make use of well-known frameworks like Matplotlib, Seaborn, and Plotly.
- In Google collab, First of all we Changed runtime from TPU to GPU.      
- We cross checked it by running command ‘!nvidia-smi’                                                                      
#### Coding
- First of all, We installed Yolov8 by the command ‘!pip install ultralytics==8.0.20’
- Further we checked about Yolov8 by the command ‘from ultralytics import YOLO from IPython.display import display, Image’      
- Then we connected and mounted our google drive account by the code ‘from google.colab import drive drive.mount('/content/drive')’
- Then we ran our main command to run the training process ‘%cd /content/drive/MyDrive/Accident Detection model !yolo task=detect mode=train model=yolov8s.pt data= data.yaml epochs=1 imgsz=640 plots=True’
- After the training we ran command to test and validate our model ‘!yolo task=detect mode=val model=runs/detect/train/weights/best.pt data=data.yaml’
‘!yolo task=detect mode=predict model=runs/detect/train/weights/best.pt conf=0.25 source=data/test/images’
- Further to get result from any video or image we ran this command ‘!yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source="/content/drive/MyDrive/Accident-Detection-model/data/testing1.jpg/mp4"’     
- The results are stored in the runs/detect/predict folder.                                            
Hence our model is trained, validated and tested to be able to detect accidents on any video or image. 


## Challenges I ran into
#### I majorly ran into 3 problems while making this model

- I got difficulty while saving the results in a folder, as yolov8 is latest version so it is still underdevelopment. so i then read some blogs, referred to stackoverflow then i got to know that we need to writ an extra command in new v8 that ''save=true'' This made me save my results in a folder.
- I was facing problem on cvat website because i was not sure what to do to a image with no accident, after referring to some blogs and taking to some ml engineers i got to know that i should use roboflow because they have an inbuilt function in which you can mark an image null if it dont contain any accident. Thats why i used roboflow.
- I faced problem in knowing the best no. of epochs/iteration for my model which can make my model most accurate. Somehow, after some research i got to know that 150-200 is optimal no. of iteration. Also i had to do a bit of research to know whether to use nano, small or large version of YOLO.

## Results
- Accident detection demo.mp4 is Live accident detection on a video by this model 

## What we learned
- Got Practical knowledge while Working with YOLO and CNN Algorithm
- More Knowledge about Machine learning, AI and Deep leaning
- Increase in skill of making my model more accurate and fast.
- Time Management and Resource Management.

## Way Forward
- This Model can be implemented in the cameras placed on highway Pol with the help of an iot device in camera it can be used to report to the nearest control room.
- This model can also be transformed into an open source web application using Frameworks like Flask which can be used by anyone to cross check any image to know about if any accident occured in it.
