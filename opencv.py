import cv2

img = cv2.imread('lena.jpg', 0)

print(img)
cv2.imshow('my imported picture', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png',img)
    