import cv2
import os

detector = 'faceDetector.xml'
folder = 'faceData'
subfolder = 'Yash'
path = os.path.join(folder,subfolder)
os.makedirs(path,exist_ok=True)
width,height = 125,100
classify = cv2.CascadeClassifier(detector)
cam = cv2.VideoCapture(0)
count =1

while count < 31:
    boolean1,frame = cam.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = classify.detectMultiScale(grey,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
        face = grey[y:y+h,x:x+w]
        faceResize = cv2.resize(face,(width,height))
        cv2.imwrite('%s/%s.png'%(path,count),faceResize)
    count+=1
    cv2.imshow('FacesDetected!!',frame)
    if cv2.waitKey(10) == 27:
        break