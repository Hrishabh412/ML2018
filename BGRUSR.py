#!/usr/bin/python3
import cv2
import numpy as np
import sys

inn=sys.argv
w=int(inn[1])
out=int(inn[2])
q=int(inn[3])
e=int(inn[4])
f=int(inn[5])
s=int(inn[6])
r=int(inn[7])
img=cv2.imread('lambo.jpg',1)

#drawing line

output=cv2.line(img,(0,0),(w,out),(q,f,r),2)

#draw rectangle
img1=cv2.rectangle(img,(50,75),(s,out),(q,f,r),3)

#draw circle
img1=cv2.circle(img,(150,120),r,(255,0,0),2)

cv2.imshow('adhoc',output)
cv2.imshow('adhoc',img1)
cv2.waitKey(0)

