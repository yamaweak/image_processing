import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('color tone') # create win with win name

cv2.createTrackbar('R','color tone',0,255,myfunc)
cv2.createTrackbar('G','color tone',0,255,myfunc)
cv2.createTrackbar('B','color tone',0,255,myfunc)

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):

    ret, frame = cap.read()
    if not ret: continue

    r = cv2.getTrackbarPos('R','color tone')
    g = cv2.getTrackbarPos('G','color tone')
    b = cv2.getTrackbarPos('B','color tone')

    frame[:,:,0] = (255-r)/255*(255-g)/255*frame[:,:,0]
    frame[:,:,1] = (255-b)/255*(255-r)/255*frame[:,:,1]
    frame[:,:,2] = (255-g)/255*(255-b)/255*frame[:,:,2]

    cv2.imshow('color tone', frame)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()