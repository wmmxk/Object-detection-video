import cv2
cap = cv2.VideoCapture('../data/develop.mp4')
while(1):
    _ , img2=cap.read()
#    cv2.namedWindow('video',cv2.WINDOW_NORMAL)
    cv2.imshow('Video',img2)
    print("image shape:",img2.shape)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
