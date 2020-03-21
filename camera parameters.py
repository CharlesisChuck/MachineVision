import cv2

cap = cv2.VideoCapture(0)#device index for camera

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#you cannot make your camera give a resolution value out that the camera cannot provide
cap.set(3, 1208)#set value of width
cap.set(4, 720)#set value of height

print(cap.get(3))#width
print(cap.get(4))#height
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #this changes video from colors to other colors -> to gray
        cv2.imshow('video frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
