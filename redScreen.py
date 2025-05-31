import cv2
import numpy as np

back = cv2.imread('backroundScreen.jpg')

back = cv2.cvtColor(back,cv2.COLOR_BGR2HSV)

#red masks
lr1 = np.array([0,40,40])
ur1 = np.array([0,255,255])
mask1 = cv2.inRange(back,lr1,ur1)

lr2 = np.array([160,40,40])
ur2 = np.array([180,255,255])
mask2 = cv2.inRange(back,lr1,ur1)

fmask = mask2+mask1
#refining the mask 
fmask = cv2.morphologyEx(fmask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
fmask = cv2.dilate(fmask,np.ones((3,3),np.uint8),iterations=1)
fmask2 = cv2.bitwise_not(fmask)
cv2.imshow('mask1',mask1)
cv2.waitKey()
cv2.imshow('mask2',mask2)
cv2.waitKey()
cv2.imshow('maskFinal',fmask2)
cv2.waitKey()
cv2.destroyAllWindows()






















