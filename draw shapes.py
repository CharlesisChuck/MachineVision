import numpy as np
import cv2

#img = cv2.imread('lena.jpg',1)
img = np.zeros([512,512,3], np.uint8)#this creates an image 512x512 with value type uint8

img = cv2.line(img, (160,20), (160,20), (255,0,0), 10) #(the image, position1,position2,color, thickness)
#could replace line with arrowedLine
#or rectangle(img, (384,0), (510,128), (0,0,255), 5)

# font = cv2.FONT_HERSHEY_COMPLEX
# img = cv2.putText(img, "Hello World!", (10,500), font, 4, (255,255,255), 5, cv2.LINE_AA)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()