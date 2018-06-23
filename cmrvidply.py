#!usr/bin/python3

import cv2
#loading camera

cam=cv2.VideoCapture('vid.avi')

#cheking for detection

while cam.isOpened():
	print("working")
	#x,y=ca.read()
	status,frame=cam.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	cv2.imshow('camera0',frame)
	cv2.imshow('camera1',gray)
	#cv2.imshow('camera2',hsv)

	if cv2.waitKey(1) & 0xFF == ord('q') :
		break
cv2.destroyAllWindows()
cam.release()
