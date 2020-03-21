import numpy as np
import cv2
#this code puts the text and coridinates of your click when you click on the picutre
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y), 3, (0, 0, 255), -1)
        points.append((x, y))#this saves the coordinates every time we click the mouse
        if len(points) >=2:
            cv2.line(img,points[-1], points[-2], (255,255,255), 5)
        #print( x , ', ' , y )
        #font = cv2.FONT_HERSHEY_COMPLEX
        #strXY = str(x) + ', ' + str(y)
        #cv2.putText(img, strXY, (x,y), font, 1, (255,0,0),2)
        cv2.imshow('image', img)





    #if event == cv2.EVENT_RBUTTONDBLCLK:#this will print the bgr values of the spot you clicked on the picture
    #    blue = img[y,x,0]
    #    green = img[y,x,1]
    #    red = img[y,x,2]
    #    font = cv2.FONT_HERSHEY_COMPLEX
    #    strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
    #    cv2.putText(img, strBGR, (x,y), font, 1, (255,255,255),2)
    #    cv2.imshow('image', img)


#img = np.zeros((512, 512, 3), np.uint8) # this makes a black blank image
img = cv2.imread('lena.jpg')
cv2.imshow('image',img)

points = []


cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()