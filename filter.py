import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('filter') # create win with win name

cv2.createTrackbar('N', # name of value
                   'filter', # win name
                   0, # min
                   10, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue


    v = cv2.getTrackbarPos('N',  # get the value
                           'filter')  # of the win
    ## do something by using v

    if v == 0:
        cv2.imshow('filter',frame)
    else :    
        blur = cv2.blur(frame,(v,v))    
        cv2.imshow('filter', blur)

     # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()