#!/usr/bin/python3
import cv2

img1=cv2.imread('index1.jpg')
img2=cv2.imread('index2.jpg')

print(img1.shape)
print(img2.shape)
# adding image with equal contribution
# image shape must be common
# newimg=cv2.add(img1,img2)

# to add some % of image
newimg=cv2.addWeighted(img1,0.7,img2,0.3,1)
newimg1=cv2.addWeighted(img1,0.4,img2,0.6,1)
newimg2=cv2.addWeighted(img1,0.5,img2,0.5,0)
newimg3=cv2.addWeighted(img1,0.3,img2,0.7,0)

cv2.imshow('windows',newimg)
cv2.imshow('windows1',newimg1)
cv2.imshow('windows2',newimg2)
cv2.imshow('windows3',newimg3)
cv2.waitKey(0)
cv2.destroyAllWindows()


