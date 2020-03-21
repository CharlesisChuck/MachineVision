import cv2
import numpy as np





if __name__ == '__main__':
    # Read image
    img = cv2.imread("examplebeads.png")

    # Select ROI
    #r = cv2.selectROI(img)
    r = (289, 219, 133, 165)
    # Crop image
    im = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,100,200,0)

    contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    areas = []
    for contour in contours:
        if (cv2.contourArea(contour) > 20 and cv2.contourArea(contour) < 40):

            areas.append(cv2.contourArea(contour))
            cv2.drawContours(im, contour, -1, (0, 0, 255), 3)
    print(areas)
    img = cv2.drawContours(im, contours, -1, (0,255,0), 1)

    cv2.imshow('contour',img)
    cv2.waitKey(0)
    cv2.imwrite('contour.png',img)