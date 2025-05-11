#11/05/25
import cv2



#detecting edges
pika = cv2.imread('pikachu.png')
'''d = cv2.Canny(pika,1,200)
d2 = cv2.Canny(pika,100,200)
cv2.imshow('edges',d)
cv2.waitKey(0)
cv2.imshow('edgesDiff',d2)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#drawing shapes
#drawing a line
l = cv2.line(pika,(10,10),(400,400),(60,50,20),10)
cv2.imshow('line',l)
cv2.waitKey(0)
cv2.destroyAllWindows()

#rectangle

r = cv2.rectangle(pika,(90,90),(290,270),(0,255,0),5)
cv2.imshow('rect',r)
cv2.waitKey(0)
cv2.destroyAllWindows()

#circle
c = cv2.circle(pika,(190,182),110,(0,255,0),1)
cv2.imshow('rect',c)
cv2.waitKey(0)
cv2.destroyAllWindows()

#text   
t = cv2.putText(pika,'i am pikachu',(150,182),cv2.FONT_ITALIC,1,(255,255,0),5)
cv2.imshow('text',t)
cv2.waitKey(0)
cv2.destroyAllWindows()