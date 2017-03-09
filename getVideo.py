import numpy as np
import cv2
video = cv2.VideoCapture(0)
while(True):
	ret, frame = video.read()
    #Grayscale
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
    #Converts grayscale into only black or white.
    #Change second argument until camera only sees the hand
	ret,thresh1 = cv2.threshold(blur,250,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)   #change to this to get the inv color
	#ret,thresh1 = cv2.threshold(blur,250,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  
	img, contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
    #go through the length of contours, and pick out the one with the largest area
	max_area = 0
	for i in range(len(contours)):
		cnt=contours[i]
		area = cv2.contourArea(cnt)
		if(area>max_area):
			max_area=area
			ci=i;
    #ci is the chosen area
	cnt = contours[ci]

    #create a convext hull
	hull = cv2.convexHull(cnt)

  
    #Debug window that's still grayscalled
    #cv2.imshow('frame',gray)
	drawing = np.zeros(img.shape, np.uint8)
	
	cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
	cv2.drawContours(drawing,[hull],0,(0,0,255),2)
	cv2.imshow('binary',thresh1)
	cv2.imshow('outline',drawing)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# When everything done, release the capture
video.release()
cv2.destroyAllWindows()