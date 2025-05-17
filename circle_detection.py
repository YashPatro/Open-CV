#11/05/25

import cv2
import numpy as np

'''pika = cv2.imread('pikachu.png')
grey = cv2.cvtColor(pika,cv2.COLOR_BGR2GRAY)
greyB = cv2.blur(grey,(3,3))

#circle dtection
c = cv2.HoughCircles(greyB,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius= 1, maxRadius=100)

if c is not None:
    c = np.uint16(np.around(c))
    for i in c[0,:]:
        x,y,r = i[0],i[1],i[2]
        cv2.circle(pika,(x,y),r,(200,255,10),4)
        cv2.imshow('detected!',pika)
        cv2.waitKey(0)
'''
#17/05/2025
#simple blob detector 

blobs = cv2.imread('blobs2detect.jpg',0)
params = cv2.SimpleBlobDetector_Params()
#seting the area filter parameter 
params.filterByArea = True
params.minArea = 1
#filtering by circularity 
params.filterByCircularity = True
params.minCircularity = 0.6
#filtering by convexity 
params.filterByConvexity = True
params.minConvexity = 0.9
#filter by inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01
#creating a detector with the parameters 
detector = cv2.SimpleBlobDetector_create(params)

pointers = detector.detect(blobs)
kernel = np.zeros((1,1))

circles = cv2.drawKeypoints(blobs,pointers,kernel,(25,125.195))
num_blobs = len(pointers)
textStr = 'Number of circles detected: '+str(num_blobs)
text = cv2.putText(circles,textStr,(10,10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),2)
cv2.imshow('circle dector 2.0',circles)
cv2.waitKey(0)
cv2.destroyAllWindows()