import numpy as np
import cv2
video = cv2.VideoCapture(0)
while(True):
    ret, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh1 = cv2.threshold(blur,250,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow('frame',gray)
    cv2.imshow('binary',thresh1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
video.release()
cv2.destroyAllWindows()
