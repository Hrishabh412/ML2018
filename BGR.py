#!/usr/bin/python3
import cv2
import numpy as np

img=cv2.imread('index.jpeg',1)



#drawing line

img1=cv2.line (img,(0,0),(100,80),(0,0,255),2)

#draw rectangle
img1=cv2.rectangle(img,(50,75),(250,150),(1,255,0),3)

#full color
#img1=cv2.rectangle(img,(50,75),(250,150),(1,255,0),-1)

#draw circle
img1=cv2.circle(img,(150,120),100,(255,0,0),2)

#draw ellipse
img1 = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#for text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Rishabh',(10,50), font, 4,(200,255,255),2,cv2.LINE_AA)
cv2.imshow('adhoc',img1)
cv2.waitKey(0)

#for saving
cv2.imwrite('messigray.png',img)

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)

cv2.destroyAllWindows()

