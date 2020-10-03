import cv2
import numpy as np


#Callback functions to draw on image 
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
A = False #When A is true image with logo would show up 
img = cv2.imread('ronaldo.jpg')


def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,A
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
  



def insert_logo():
    if A:
        img1 = cv2.imread('ronaldo.jpg')
        img2 = cv2.imread('logo.jpg')
        rows,cols,channels = img2.shape
        roi = img1[0:rows, 0:cols ]
        img2hsv = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
        lower_blue = np.array([20,20,20])
        upper_blue = np.array([255,255,255])
        mask = cv2.inRange(img2hsv, lower_blue, upper_blue)
        mask_inv = cv2.bitwise_not(mask)
        img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
        dst = cv2.add(img1_bg,img2_fg)
        img1[0:rows, 0:cols ] = dst
        cv2.namedWindow('image with logo')
        cv2.imshow('image with logo',img1)
        cv2.waitKey(0)

    
 


cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,draw_circle_rectangle)
cv2.createTrackbar('G','image',0,255,draw_circle_rectangle)
cv2.createTrackbar('B','image',0,255,draw_circle_rectangle)
cv2.setMouseCallback('image',draw_circle_rectangle)
#    cv2.namedWindow('image with logo')
#    cv2.imshow('image with logo',img1)



while(1):
    cv2.imshow('image',img)

    k = cv2.waitKey(1) & 0xFF
    
    if k == ord('m'):
        mode = not mode
    elif k == ord('a'):
        A = not A
        insert_logo()
    elif k == 27:
        break
       
        
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
cv2.destroyAllWindows()
