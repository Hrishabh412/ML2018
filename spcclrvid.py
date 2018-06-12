#!/usr/bin/python3

import cv2

cap=cv2.VideoCapture(0)
'''
img=cv2.imread('index.jpeg')

#print(img.shape())

#only picking red color

only_red=cv2.inRange(img,(0,0,40),(20,20,255))

cv2.imshow('win',only_red)
'''
while cap.isOpened():
	status,frame=cap.read()
	onlyred=cv2.inRange(frame,(0,0,40),(20,20,255))
	onlyblue=cv2.inRange(frame,(40,0,0),(255,20,20))
	onlygreen=cv2.inRange(frame,(0,40,0),(20,255,20))

	cv2.imshow('frame',frame)
	cv2.imshow('frame1',onlyred)
	cv2.imshow('frame2',onlyblue)
	cv2.imshow('frame3',onlygreen)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
			break

cv2.destroyAllWindows()
cam.release()
