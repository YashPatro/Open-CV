import cv2
import numpy as np
import os


detector = 'faceDetector.xml'
folder = 'faceData'
subfolder = 'Person1'
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
print(face,lable) 





