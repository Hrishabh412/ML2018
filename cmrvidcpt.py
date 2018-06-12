#!/usr/bin/python3
import numpy as np
import cv2

cam=cv2.VideoCapture(0)


#deciding video format

vid_format=cv2.VideoWriter_fourcc(*'xvid')

		   #filename  ,video format,FPS,video W,H
out=cv2.VideoWriter('output.avi',vid_format,5.0,(640,480))

print(cv2.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cv2.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cam.isOpened():
	status,frame=cam.read()
	cv2.imshow('frame',frame)
	out.write(frame)

	
	if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	

cam.release()
cv2.destroyAllWindows()
