import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

img = cv2.imread('examplebeads.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5) , np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)#this is made to remove high frequesncy noise
#use this for removing salt and pepper noise
mblur = cv2.medianBlur(img,5)
bilat = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['images', '2D Convolutions', 'blur', 'Gaussian blur', 'Median Blur', 'bilateralfilter','images2','images3','image4s','imag5es']
images = [img,dst, blur,gblur,mblur,bilat,dst,dst,dst,dst]

list_size = len(images)
columns = int(math.sqrt(list_size))
row = math.ceil(list_size / columns)

for i in range(list_size):
    plt.subplot(columns,row,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

# Image_List = [test, keypoints_im, img]
# Image_Names = ["Original", "Keypoints", "blah"]
#
# list_size = len(Image_List)
# columns = int(math.sqrt(list_size))
# row = math.ceil(list_size / columns)
# for i in range(list_size):
#     plt.subplot(columns, row, i + 1), plt.imshow(Image_List[i], 'gray')
#     plt.title(Image_Names[i])
#     plt.xticks([]), plt.yticks([])
# cv.waitKey(0)