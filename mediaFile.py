'''#28/06/25
import cv2
import mediapipe as mp

#initialising mediapipe face detection
faceDetect = mp.solutions.face_detection
drawing = mp.solutions.drawing_utils
actualDetection = faceDetect.FaceDetection(min_detection_confidence = 0.9)
cam = cv2.VideoCapture(0)
while cam.isOpened():
    boolean,frame = cam.read()
    if not boolean:
print('failed to grab frame')
        break 
    rgbImg = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #processin g img and detecting the face
    result = actualDetection.process(rgbImg)
    #draw face landmarks on the frame
    if result.detections:
        for i in result.detections:
            drawing.draw_detection(frame,i)

    cv2.imshow('frame',frame)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()'''
#hw
import pygame
pygame.init()
pygame.mixer.init()
import cv2
import mediapipe as mp

ring = pygame.mixer.Sound('ringtone.mp3')


# Initialising mediapipe face detection
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
    # Processing image and detecting faces
    result = actualDetection.process(rgbImg)
    if result.detections and not faceDetected:
        ring.play()
        faceDetected = True
    elif not result.detections:
        faceDetected = False
    # Count the number of faces detected
    num_faces = 0
    if result.detections:
        for i in result.detections:
            drawing.draw_detection(frame, i)
            num_faces += 1

    # Display the number of faces on the frame
    cv2.putText(frame, f"Faces detected: {num_faces}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow('Frame', frame)

    # Exit if the ESC key is pressed
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
