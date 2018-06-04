#!/usr/bin/python3
import numpy as np
import cv2

cam=cv2.VideoCapture(0)

#define the codecand object
fourcc=cv2.VideoWriter_fourcc(*'xvid')
out=cv2.VideoWriter('output.avi',fourcc,10.0,(640,480))

while cam.isOpened():
	status,frame=cam.read()
	if status == True:
		frame=cv2.flip(frame,0)

#write the flipped frame
		out.write(frame)

		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cam.release()
out.release()
cv2.destroyAllWindows()
