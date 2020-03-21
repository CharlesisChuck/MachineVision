import cv2
cap = cv2.VideoCapture('Bead_Data/190719 EML0137 no pairing.avi')
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow('window-name',frame)
    cv2.imwrite("Output_Files/frame%d.jpg" % count, frame)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()  # destroy all the opened windows