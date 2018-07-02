import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('tonecurve') # create win with win name

cv2.createTrackbar('tone', # name of value
                   'tonecurve', # win name
                   0, # min
                   10, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue
        
    v = cv2.getTrackbarPos('tone',  # get the value
                           'tonecurve')  # of the win
    ## do something by using v
    y = (np.sin(np.pi*(v/255-0.5))+1)/2*25
    
    tone = y * frame

    cv2.imshow('tonecurve', tone)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()