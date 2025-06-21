#31/05/25
import cv2
import numpy as np

vid = cv2.VideoCapture(0)
background = None 
for i in range(60):
    boolean1,frame = vid.read()
    if boolean1 == False:
        continue
    frame = cv2.flip(frame,1)
    background = frame
while (vid.isOpened()):
    boolean1,img = vid.read()
    if not boolean1:
        break
    hsvimg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


    #red masks
    lr1 = np.array([0,50,50])
    ur1 = np.array([0,255,255])
    mask1 = cv2.inRange(hsvimg,lr1,ur1)

    lr2 = np.array([160,40,40])
    ur2 = np.array([180,255,255])
    mask2 = cv2.inRange(hsvimg,lr2,ur2)

    fmask = mask1+mask2
    #refining the mask 
    fmask = cv2.morphologyEx(fmask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    fmask = cv2.dilate(fmask,np.ones((3,3),np.uint8),iterations=1)
    fmask2 = cv2.bitwise_not(fmask)
    result1 = cv2.bitwise_and(background,background,mask=fmask)
    result2 = cv2.bitwise_and(img,img,mask=fmask2) 
    finalO = cv2.addWeighted(result1,1,result2,1,0)
    finalO = cv2.rotate(finalO,cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('final',finalO)
    k = cv2.waitKey(10)
    if k == 27:
        break
