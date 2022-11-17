import cv2
import numpy as np
import keyboard
 
cv2.namedWindow("Camera Preview")
vc = cv2.VideoCapture(0) #camera video
faceCascade = cv2.CascadeClassifier(r"C:\Users\Light\Desktop\haarcascade_frontalface_default.xml")
 
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
 
while rval:
    flipHorizontal = cv2.flip(frame,1)
    # flipHorizontal = cv2.cvtColor(flipHorizontal,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(flipHorizontal, 1.3,5)
    for (x, y, w, h) in faces:
        cv2.rectangle(flipHorizontal, (x, y), (x+w, y+h), (0, 0, 255), 2)
 
    cv2.imshow("Camera Preview", flipHorizontal)
    # cv2.rectangle(flipHorizontal,(384,0),(510,128),(0,255,0),3)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
 
vc.release()
cv2.destroyWindow("Camera Preview")