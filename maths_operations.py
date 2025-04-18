import cv2


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
cv2.destroyAllWindows()