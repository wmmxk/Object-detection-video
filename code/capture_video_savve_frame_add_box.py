import cv2  # OpenCV Library
from random import randint
import numpy as np
from PIL import Image
#-----------------------------------------------------------------------------
#       Load and configure Haar Cascade Classifiers
#-----------------------------------------------------------------------------
 
# location of OpenCV Haar Cascade Classifiers:
baseCascadePath = "/usr/local/share/OpenCV/haarcascades/"
 
# xml files describing our haar cascade classifiers
faceCascadeFilePath = baseCascadePath + "haarcascade_frontalface_default.xml"
noseCascadeFilePath = baseCascadePath + "haarcascade_mcs_nose.xml"
 
# build our cv2 Cascade Classifiers
faceCascade = cv2.CascadeClassifier(faceCascadeFilePath)
noseCascade = cv2.CascadeClassifier(noseCascadeFilePath)

 
#-----------------------------------------------------------------------------
#       Main program loop
#-----------------------------------------------------------------------------
 
# collect video input from first webcam on system
video_capture = cv2.VideoCapture(0)
 
while True:
    # Capture video feed
    ret, frame = video_capture.read()
 
    # Create greyscale image from the video feed
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    im_back = Image.fromarray(gray)
    im_back.save('../out_data/camera_shot.jpg')
    # Detect faces in input video stream
     
   # Iterate over each face found
    box = cv2.rectangle(frame,(10,10),(100,80),(255,0,0),2)
 
 
    # Display the resulting frame
    cv2.imshow('Video', frame)
 
    # press any key to exit
    # NOTE;  x86 systems may need to remove: " 0xFF == ord('q')"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
