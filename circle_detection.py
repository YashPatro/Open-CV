#11/05/25

import cv2
import numpy as np

pika = cv2.imread('pikachu.png')
grey = cv2.cvtColor(pika,cv2.COLOR_BGR2GRAY)
greyB = cv2.blur(grey,(3,3))

#circle dtection
c = cv2.HoughCircles(greyB,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius= 1, maxRadius=1000)

if c is not None:
    c = np.uint16(np.around(c))
    for i in c[0,:]:
        x,y,r = i[0],i[1],i[2]
        cv2.circle(pika,(x,y),r,(200,255,10),4)
        cv2.imshow('detected!',pika)
        cv2.waitKey(0)

