import cv2 as cv
import numpy as np

#first thing is to use the recoding of our video
video = "190719 EML0137 doublet.avi"
cap = cv.VideoCapture(video)#device index for camera
#fourcc = cv.VideoWriter_fourcc(*'XVID')
#out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #this changes video from colors to other colors -> to gray
        cv.imshow('video frame', gray)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
