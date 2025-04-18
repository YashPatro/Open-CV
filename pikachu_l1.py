import cv2
x = cv2.imread('pikachu.png')
#greyscale
'''x = cv2.imread('pikachu.png',0)
cv2.imshow('Pikachu',x)
cv2.waitKey(0)
'''#splitting an image into its bgr saturations
b,g,r = cv2.split(x)
cv2.imshow('orignal',x)
cv2.waitKey(0)
cv2.imshow('BlueSat',b)
cv2.waitKey(0)
cv2.imshow('RedSat',r)
cv2.waitKey(0)
cv2.imshow('GreenSat',g)
cv2.waitKey(0)

cv2.destroyAllWindows()
#dimensions
print(x.shape)