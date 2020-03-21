import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('water.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5) , np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)#this is made to remove high frequesncy noise
#use this for removing salt and pepper noise
mblur = cv2.medianBlur(img,5)
bilat = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['images', '2D Convolutions', 'blur', 'Gaussian blur', 'Median Blur', 'bilateralfilter']
images = [img,dst, blur,gblur,mblur,bilat]

for i in range(6):
    plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()