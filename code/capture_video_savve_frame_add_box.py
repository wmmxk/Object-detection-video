import cv2  # OpenCV Library

# collect video input from first webcam on system
video_capture = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    # Capture video feed
    ret, frame = video_capture.read()

     
   # Iterate over each face found
    box = cv2.rectangle(frame,(10,10),(400,80),(255,0,0),2)

    cv2.putText(frame,'Hello World!',(10,20), font, 1,(255,255,0),2)

 
    # Display the resulting frame
    cv2.imshow('Video', frame)
 
    # press any key to exit
    # NOTE;  x86 systems may need to remove: " 0xFF == ord('q')"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
