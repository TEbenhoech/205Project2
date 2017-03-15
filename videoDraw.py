"""
##############################################################################
## Title: videoDraw.py
##    Abstract: Draw using your hand! using openCV with an XML to recognize the fist
##        you can draw to screen using your hand. use the interface on the sides to change settings
##        using your hand!
##    Note: background is important. busy backgrounds or not enough light can result in poor
##        hand recognition. Face will also sometimes be recognized, so remember to stay out of frame
##    date:3.16.2017
##    by: Team 240
##    Contributors: 
##        Harlan Cheer
##        Theo Ebenhoech
##        Gabe Gaerlan
##        Samuel Valdez 
##############################################################################
"""
import cv2
import numpy as np
import math
video = cv2.VideoCapture(0)
##Code based off code from opencv doc: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_mouse_handling/py_mouse_handling.html
ret, frame = video.read()
hand_cascade = cv2.CascadeClassifier('fist.xml')
height, width = frame.shape[:2]
drawing = False # true if mouse is pressed
mode = False # FOR MOUSE if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1   #FOR MOUSE 
brushSize = 8   #changed during collision
b= 0            
g = 0           #default colors
r = 200


# mouse callback function, based off openCV tutorial
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
#            
     
def collision_detect((center_x,center_y), pos_x, pos_y):
    collisionX = pos_x - center_x
    collisionY = pos_y - center_y
    distance = math.sqrt((collisionX * collisionX) + (collisionY * collisionY))
    return distance
     
# clear the screen       
img = np.zeros((height,width,3), np.uint8)
##init the window named image
cv2.namedWindow('image')
##register the callback mouse draw
cv2.setMouseCallback('image',draw_circle)
##the image to be used as the ui overlay
ui = cv2.imread("UI.png")

while(1):
    #center position of the hand frame
    posX = 0
    posY = 0
    ## set up the video
    ret, frame = video.read()
    
    
    #add any drawn images from the mouse draw
    both = cv2.add(frame, img)
    #use the xml to find the hand in the frame
    hand = hand_cascade.detectMultiScale(frame,1.3,4)
    
    
    for(x,y,w,h) in hand:
        #draws a rectangle around the 
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)
        #sets the position to the middle of the fist
        posX = x+(w/2)
        posY = y+(h/2)
        #set a scale?
    
    

    
    """
    see how far the fist is from a UI element
    first say where the UI element is ( this is flipped about center-y, so x = 0 is actually x = width)
    find the x and y difference
    find the distance using sqrt(x^2) + (y^2)
    set a flag to True, if needed
    check compare the distance, if it's roughly less then 35, it collides
    """
    
    eraser = (600,220)
    collisionX = posX - eraser[0]
    collisionY = posY - eraser[1]
    eraserCollision = math.sqrt((collisionX * collisionX) + (collisionY * collisionY))
    eraseFlag = True
    if eraserCollision < 35:#you can change this if you like to make the radius wider but 30 works well
        eraseFlag = False
    
    save = (310,50)
    colX = posX - save[0]
    colY = posY - save[1]
    saveCollision = math.sqrt((colX * colX)+ (colY * colY))
    saveFlag = True
    if saveCollision < 30:
        saveFlag = False
    
    small = (600,65)
    smallColX = posX - small[0]
    smallColY = posY - small[1]
    smallCollision = math.sqrt((smallColX * smallColX)+ (smallColY * smallColY))
    if smallCollision < 35:
        brushSize = 3
    
    norm = (600,100)#x, y coordiniates 
    normColX = posX - norm[0]
    normColY = posY - norm[1]
    normCollision = math.sqrt((normColX * normColX)+ (normColY * normColY))
    if normCollision < 35:
        brushSize = 8
    
    big = (600,150)
    bigColX = posX - big[0]
    bigColY = posY - big[1]
    bigCollision = math.sqrt((bigColX * bigColX)+ (bigColY * bigColY))
    if bigCollision < 35:
        brushSize = 15
    
    red = (35,40)
    redX = posX - red[0]
    redY = posY - red[1]
    redCollision = math.sqrt((redX * redX)+ (redY * redY))
    if redCollision < 35:
        g = 0
        r = 200
        b = 0



    
    orange = (35,90)
    orangeX = posX - orange[0]
    orangeY = posY - orange[1]
    orangeCollision = math.sqrt((orangeX * orangeX)+ (orangeY * orangeY))
    if orangeCollision < 35:
        g = 100
        r = 255
        b = 0




    yellow = (35,150)
    yellowX = posX - yellow[0]
    yellowY = posY - yellow[1]
    yellowCollision = math.sqrt((yellowX * yellowX)+ (yellowY * yellowY))
    if yellowCollision < 35:
        g = 255
        r = 255
        b = 0
    
    green = (35,220)
    greenX = posX - green[0]
    greenY = posY - green[1]
    greenCollision = math.sqrt((greenX * greenX)+ (greenY * greenY))
    if greenCollision < 35:
        g = 200
        r = 0
        b = 0

    blue = (35,250)
    blueX = posX - blue[0]
    blueY = posY - blue[1]
    blueCollision = math.sqrt((blueX * blueX)+ (blueY * blueY))
    if blueCollision < 35:
        g = 0
        r = 0
        b = 200
    
    violet = (35,360)
    violetX = posX - violet[0]
    violetY = posY - violet[1]
    violetCollision = math.sqrt((violetX * violetX)+ (violetY * violetY))
    if violetCollision < 35:
        g = 0
        r = 200
        b = 255
   
    #draw a circle of the brushSize and of the RGB
    cv2.circle(img,(posX,posY),brushSize,(b,g,r),-1)
    k = cv2.waitKey(1) & 0xFF #poll events
    if(eraseFlag == False or k == ord('c')): ##either flag flipped or c is pressed
        img = np.zeros((height,width,3), np.uint8) ##clears the screen
    if(saveFlag == False or k == ord('s')):
        cv2.imwrite('test.jpg',both) ##save the screen
    if k == ord('m'):
        mode = not mode ##changes the draw mode for Mouse 
    elif k == 27 or k == ord('q'): ##end program
        break
    
    frame = cv2.add(frame,ui)   ##combine the frame and the UI
    both = cv2.add(frame, img)  ##combine the drawn image and the video frame
    
    ##flip for better coordination
    both = cv2.flip(both, 1)
    ##show the video to window image
    cv2.imshow('image',both)

cv2.destroyAllWindows()