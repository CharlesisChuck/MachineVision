#4 steps
# 1. use edge detection (canny)
# 2. mapping of edge points ot teh Hough space and store in accumulator
# 3. interpretation of accumulator to yield lines of infinite length.
# the interpretation is done by thresholding and possibly other contraints
# 4. Conversion of infinite lines to finite lines

import cv2 as cv
import numpy as np

original = cv.imread('sudoku.png')
img = cv.imread('sudoku.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize=3)
cv.imshow("canny",edges)
lines = cv.HoughLines(edges,1, np.pi/180, 200)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    #x1 stores the rounded off value of (r * cos(theta)) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    #y1 stores the rounded off value of (r * sin(theta) _ 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores the rounded off value of (r * cos(theta) + 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    #y2 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))
    cv.line(img, (x1,y1), (x2,y2), (0,0,255),2)

cv.imshow('image_original',original)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()