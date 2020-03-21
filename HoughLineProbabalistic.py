#4 steps
# 1. use edge detection (canny)
# 2. mapping of edge points ot teh Hough space and store in accumulator
# 3. interpretation of accumulator to yield lines of infinite length.
# the interpretation is done by thresholding and possibly other contraints
# 4. Conversion of infinite lines to finite lines

import cv2 as cv
import numpy as np

original = cv.imread('sudoku.png')
cv.imshow('image_original',original)
img = cv.imread('sudoku.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize=3)
cv.imshow("canny",edges)
lines = cv.HoughLinesP(edges,1, np.pi/180, 100,minLineLength=100,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img, (x1,y1), (x2,y2), (0,0,255),2)


cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()