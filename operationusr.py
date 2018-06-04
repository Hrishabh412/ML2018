#!/usr/bin/python3
import cv2
import sys

inn=sys.argv

x=float(inn[1])
y=float(inn[2])
z=float(inn[3])
a=float(inn[4])

img1=cv2.imread('index1.jpg')
img2=cv2.imread('index2.jpg')

# adding image with equal contribution
# image shape must be common
# newimg=cv2.add(img1,img2)

# to add some % of image

newimg=cv2.addWeighted(img1,x,img2,y,0)
newimg1=cv2.addWeighted(img1,z,img2,a,0)

cv2.imshow('w1',newimg)
cv2.imshow('w2',newimg1)

cv2.waitKey(0)
cv2.destroyAllWindows()
