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
''''''
#median blur
imgToBlur = cv2.imread('blurring_prac.png')
median_blur = cv2.medianBlur(imgToBlur,5)
cv2.imshow('Median Blur',median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#10/05/25
'''opencv = cv2.imread('butterfly.jpeg')
blur = cv2.bilateralFilter(opencv,9,75,75)
cv2.imshow('Orginal',opencv)
cv2.waitKey(0)
cv2.imshow('Blurred',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#bordering an image
'''
newimg = cv2.imread('pikachu.png')
borderImg = cv2.copyMakeBorder(newimg,10,10,10,10,cv2.BORDER_CONSTANT,value=(20,30,40))
cv2.imshow('Old',newimg)
cv2.waitKey(0)
cv2.imshow('New',borderImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#greyscale

#img  = cv2.cvtColor(newimg,cv2.COLOR_BGR2GRAY)
'''row,column = newimg.shape[0:2]
for i in range(row):
    for j in range(column):
        newimg[i,j] = sum(newimg[i,j])/3

print(newimg.shape)
cv2.imshow('GRey',newimg)
cv2.waitKey(0)
'''
#rotating image

winter = cv2.imread('winter_back.jpg')
row,column = winter.shape[0:2]
m = cv2.getRotationMatrix2D((column/2,row/2),45,1)
s = cv2.warpAffine(winter,m,(column,row))
cv2.imshow('rotated',s)
cv2.waitKey(0)