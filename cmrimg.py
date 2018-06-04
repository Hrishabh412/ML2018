#!usr/bin/python3

import cv2
#loading camera

cam=cv2.VideoCapture(0)

#cheking for detection
#x,y=ca.read()
status,frame=cam.read()
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
cv2.imshow('camera0',frame)
cv2.imshow('camera1',gray)

cv2.waitKey(0)
cam.release()
cv2.destroyAllWindows()
