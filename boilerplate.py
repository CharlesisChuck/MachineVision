# import cv2
# import numpy as np
# from matplotlib import  pyplot as plt
#
# img = cv2.imread("messi5.jpg",0)
#
# titles = ['image']
# images = [img]
#
# for i in range(1):
#     plt.subplot(1, 1, i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()
#
#
# import cv2
# import numpy as np
#
# img = cv2.imread("messi5.jpg")
#
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

from math import *

list_length = 8
columns = int(sqrt(list_length))
rows = ceil(list_length/columns)
value = 1

if(list_length < 10):
    value = 0
if (rows * columns > list_length + value):
    if(columns < rows):
        columns = columns + 1
        if(columns < rows):
            rows = rows - 1


print(columns,rows)