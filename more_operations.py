#19/04/25

import cv2
import numpy as np

#pika = cv2.imread('eroding_prac.png')
#kernel = np.ones((5,5),np.uint8)



#eroding image
'''erode = cv2.erode(pika,kernel)
cv2.imshow('og image',pika)
cv2.waitKey(0)
cv2.imshow('Eroded Image', erode)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#GaussianBlur image
'''opencv = cv2.imread('blurring_prac.png')
blur = cv2.GaussianBlur(opencv,(7,7),0)
cv2.imshow('Orginal',opencv)
cv2.waitKey(0)
cv2.imshow('Blurred',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#median blur
imgToBlur = cv2.imread('blurring_prac.png')
median_blur = cv2.medianBlur(imgToBlur,5)
cv2.imshow('Median Blur',median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()