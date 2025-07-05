#05/07/25
import pygame
pygame.init()
pygame.mixer.init()
import cv2
import mediapipe as mp

ring = pygame.mixer.Sound('ringtone.mp3')


faceDetect = mp.solutions.face_detection
drawing = mp.solutions.drawing_utils
actualDetection = faceDetect.FaceDetection(min_detection_confidence=0.9)
cam = cv2.VideoCapture(0)
faceDetected = False


while cam.isOpened():
    boolean, frame = cam.read()
    if not boolean:
        print('Failed to grab frame')
        break
    
    rgbImg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #Processing image and detecting faces
    result = actualDetection.process(rgbImg)
    if result.detections and not faceDetected:
        ring.play()
        faceDetected = True
    elif not result.detections:
        faceDetected = False

    num_faces = 0
    if result.detections:

        for i in result.detections:
            details = i.location_data.relative_bounding_box
            h,w,c = frame.shape
            x = int(details.xmin*w)
            y = int(details.ymin*h)
            width = int(details.width*w)
            height = int(details.height*h)
            centrex = x+width//2
            centrey = y+height//2
            radius  = min(width,height)//3
            cv2.circle(frame,(centrex,centrey),radius,(0,255,255),-1)
            cv2.circle(frame,(centrex-10,centrey-10),5,(0,0,0),-1)
            cv2.circle(frame,(centrex+10,centrey-10),5,(0,0,0),-1)
            cv2.ellipse(frame,(centrex,centrey+5),(10,5),0,0,180,(0,0,0),2)
    # Display the number of faces on the frame
    cv2.putText(frame, f"Faces detected: {num_faces}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow('Frame', frame)

    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
