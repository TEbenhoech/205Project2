import numpy as np
import cv2
video = cv2.VideoCapture(0)
fist_cascade = cv2.CascadeClassifier('fist.xml')
while(True):
    ret, frame = video.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fist = fist_cascade.detectMultiScale(gray,1.3,5)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #Converts grayscale into only black or white.
    #Change second argument until camera only sees the hand
    ret,thresh1 = cv2.threshold(blur,250,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #Debug window that's still grayscalled
    for(x,y,w,h) in fist:
        #draws a rectangle around the 
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)




    cv2.imshow('frame',frame)
    cv2.imshow('binary',thresh1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
video.release()
cv2.destroyAllWindows()