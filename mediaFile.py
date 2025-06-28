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
cv2.destroyAllWindows()