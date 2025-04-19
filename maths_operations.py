#18/04/25
import numpy as np
import cv2
'''

winter = cv2.imread('winter_back.jpg')
planet = cv2.imread('planet_back.jpg')
#add/merge
merge = cv2.addWeighted(winter,0.6,planet,0.6,0)
cv2.imshow('Merged Img',merge)
cv2.waitKey(0)
#substract
sub = cv2.subtract(winter,planet)
cv2.imshow('subtracted',sub)
cv2.waitKey(0)
#resize
p = cv2.imread('pikachu.png')
rp = cv2.resize(p,(500,500))
cv2.imshow('Resuze pikachu',rp)
cv2.waitKey(0)
cv2.imshow('Resoze pikachu',p)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

clr1 = np.array([177,235,52])
clr2 = np.array([235,52,119])
#adding
'''
img1 = np.full((300,300,3),clr1,dtype=np.uint8)
img2 = np.full((300,300,3),clr2,dtype=np.uint8)
add1 = cv2.add(img1,img2)

addedImg = img1+img2
clrMix = np.concatenate((img1,img2,add1,addedImg),axis = 1)
cv2.imshow('All THe Colours', clrMix)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#subtrating

img1 = np.full((300,300,3),clr1,dtype=np.uint8)
img2 = np.full((300,300,3),clr2,dtype=np.uint8)
CvTWOsubtract = cv2.subtract(img1,img2)

subtractImg = img1-img2
clrMix = np.concatenate((img1,img2,CvTWOsubtract,subtractImg),axis = 1)
cv2.imshow('All THe Colours', clrMix)
cv2.waitKey(0)
cv2.destroyAllWindows()


