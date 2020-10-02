import cv2

#importing images 
img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')

#Callback functions to draw on image 
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
def draw_circle_resctangle(event,x,y,flags,params):
    global drawing,mode,ix,iy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
  
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix,iy), (x,y) , (0,0,0) , -1)
            elif mode == False:
                cv2.circle(img, (x,y), 30, (250,250,250) , -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),30,(0,0,255),-1)
