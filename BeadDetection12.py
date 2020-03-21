import cv2 as cv
import numpy as np

original = cv.imread('examplebeads.png')
cv.imshow('image_original',original)
img = cv.imread('examplebeads.png')


# Select ROI
#r = cv.selectROI(img)
r = (289, 219, 133, 165)
# Crop image
im = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]




gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,30,35,apertureSize=3)
cv.imshow("canny",edges)
lines = cv.HoughLinesP(edges,1, np.pi/180, 40,minLineLength=3,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(im, (x1,y1), (x2,y2), (0,0,255),2)


cv.imshow('image',im)
cv.waitKey(0)
cv.destroyAllWindows()