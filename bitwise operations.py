import cv2
import numpy as np

img1 = np.zeros((512,512,3), np.uint8)
img2 = cv2.rectangle(img1,(200,0), (300,100), (255,255,255), -1)
img2 = cv2.imread("lena.jpg")

#bitAnd = cv2.bitwise_and(img2,img1)
#bitAnd = cv2.bitwise_or(img2,img1)
#bitAnd = cv2.bitwise_not(img2,img1)
bitAnd = cv2.bitwise_xor(img2,img1)

cv2.imshow("img1",img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAnd", bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()