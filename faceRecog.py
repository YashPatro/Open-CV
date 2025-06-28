import cv2

import numpy as np
import os


detector = 'faceDetector.xml'
folder = 'faceData'
subfolder = 'Person1'
width,height = 110,130
print('Please ensure sufficient lighting for the webcam to detect face.')
(face,lable,d1,id) = ([],[],{},0)
if not os.path.exists(folder) or not os.listdir(folder):
    print('directory is empty or it doesnt exist')
for i in os.listdir(folder):
    path = os.path.join(folder,i)
    if os.path.isdir(path):
        d1[id]= i
        for  i in os.listdir(path):
            pathImg = os.path.join(path,i)
            img = cv2.imread(pathImg,0)
            face.append(img)
            lable.append(id)
        id+=1
(face,lable) = [np.array(i) for i in [face,lable]]

recogniser = cv2.face.LBPHFaceRecognizer_create()
recogniser.train(face,lable)
clasify = cv2.CascadeClassifier(detector)
cam = cv2.VideoCapture(0)
while True:
    boolean1,frame = cam.read()
    if not boolean1 or frame is None:
        print('error')
        continue
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = clasify.detectMultiScale(grey,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
        face = grey[y:y+h,x:x+w]
        faceResize = cv2.resize(face,(width,height))    
        prediction = recogniser.predict(faceResize)
        if prediction[1]<100:
            cv2.putText(frame,f'{d1[prediction[0]]} - {prediction[1]:.0f}',(x+30,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)
        else:
            cv2.putText(frame,'Unknown',(x+30,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)
