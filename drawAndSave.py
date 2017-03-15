import cv2
import numpy as np
import math
video = cv2.VideoCapture(0)
##Code based off code from opencv doc: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_mouse_handling/py_mouse_handling.html
ret, frame = video.read()
hand_cascade = cv2.CascadeClassifier('fist.xml')
height, width = frame.shape[:2]
drawing = False # true if mouse is pressed
mode = False # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
brushSize = 8
b= 0
g = 0
r = 200

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
            
            
img = np.zeros((height,width,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
ui = cv2.imread("UI.png")

while(1):
   
    posX = 0
    posY = 0
    ret, frame = video.read()
    
    
    both = cv2.add(frame, img)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hand = hand_cascade.detectMultiScale(gray,1.3,4)
    
    blur = cv2.GaussianBlur(gray,(5,5),0)
    
    

    for(x,y,w,h) in hand:
        #draws a rectangle around the 
        cv2.rectangle(frame,(x,y),(x+w, y+h),(b,g,r),2)
        posX = x+(w/2)
        posY = y+(h/2)
    
    eraser = (600,220, 0)
    collisionX = posX - eraser[0]
    collisionY = posY - eraser[1]
    eraserCollision = math.sqrt((collisionX * collisionX) + (collisionY * collisionY))
    eraseFlag = True
    if eraserCollision < 35:#you can change this if you like to make the radius wider but 30 works well
        eraseFlag = False
    
    save = (310,50,0)
    colX = posX - save[0]
    colY = posY - save[1]
    saveCollision = math.sqrt((colX * colX)+ (colY * colY))
    saveFlag = True
    if saveCollision < 30:
        saveFlag = False
    
    small = (600,65,0)
    smallColX = posX - small[0]
    smallColY = posY - small[1]
    smallCollision = math.sqrt((smallColX * smallColX)+ (smallColY * smallColY))
    if smallCollision < 35:
        brushSize = 3
    
    norm = (600,100,0)#x, y coordiniates 
    normColX = posX - norm[0]
    normColY = posY - norm[1]
    normCollision = math.sqrt((normColX * normColX)+ (normColY * normColY))
    if normCollision < 35:
        brushSize = 8
    
    big = (600,150,0)
    bigColX = posX - big[0]
    bigColY = posY - big[1]
    bigCollision = math.sqrt((bigColX * bigColX)+ (bigColY * bigColY))
    if bigCollision < 35:
        brushSize = 15
    
    red = (35,40,0)
    redX = posX - red[0]
    redY = posY - red[1]
    redCollision = math.sqrt((redX * redX)+ (redY * redY))
    if redCollision < 35:
        g = 0
        r = 200
        b = 0



    
    orange = (35,90,0)
    orangeX = posX - orange[0]
    orangeY = posY - orange[1]
    orangeCollision = math.sqrt((orangeX * orangeX)+ (orangeY * orangeY))
    if orangeCollision < 35:
        g = 100
        r = 255
        b = 0




    yellow = (35,150,0)
    yellowX = posX - yellow[0]
    yellowY = posY - yellow[1]
    yellowCollision = math.sqrt((yellowX * yellowX)+ (yellowY * yellowY))
    if yellowCollision < 35:
        g = 255
        r = 255
        b = 0
    
    green = (35,220,0)
    greenX = posX - green[0]
    greenY = posY - green[1]
    greenCollision = math.sqrt((greenX * greenX)+ (greenY * greenY))
    if greenCollision < 35:
        g = 200
        r = 0
        b = 0

    blue = (35,250,0)
    blueX = posX - blue[0]
    blueY = posY - blue[1]
    blueCollision = math.sqrt((blueX * blueX)+ (blueY * blueY))
    if blueCollision < 35:
        g = 0
        r = 0
        b = 200
    
    violet = (35,360,0)
    violetX = posX - violet[0]
    violetY = posY - violet[1]
    violetCollision = math.sqrt((violetX * violetX)+ (violetY * violetY))
    if violetCollision < 35:
        g = 0
        r = 200
        b = 255
   
    
    cv2.circle(img,(posX,posY),brushSize,(b,g,r),-1)
    #cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if(eraseFlag == False):
        img = np.zeros((height,width,3), np.uint8) 
    if(saveFlag == False):
        cv2.imwrite('test.jpg',both)
    if k == ord('m'):
        mode = not mode
    if k == ord('s'):
        cv2.imwrite('test.jpg',both)
    if k == ord('c'):
        img = np.zeros((height,width,3), np.uint8)    
    elif k == 27 or k == ord('q'):
        break
    
    frame = cv2.add(frame,ui)
    both = cv2.add(frame, img)
    

    both = cv2.flip(both, 1)
    cv2.imshow('image',both)

cv2.destroyAllWindows()