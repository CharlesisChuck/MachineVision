import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5,2),np.uint8)
dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal, iterations=2)#erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal, iterations=2)#dilation followed by erosion

test = cv2.morphologyEx(mask, cv2.MORPH_ELLIPSE, kernal, iterations=2)#
#test = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal, iterations=2)#
#test = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal, iterations=2)#findes thresholds


titles = ['image', 'mask', 'dilation', 'erosions', 'opening','closing','test']
images =  [img, mask, dilation, erosion, opening,closing,test]

for i in range(7):
    plt.subplot(3,3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()