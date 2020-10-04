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
color = (0,0,0)
def draw_circle_rectangle(event,x,y,flags,param): 
    global ix,iy,drawing,mode,color

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
            else:
                cv2.circle(img,(x,y),5,(b,g,r),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
        else:
            cv2.circle(img,(x,y),5,(b,g,r),-1)


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

def scan_and_filter():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Camera")
    while True:
        img_counter = 0
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Camera", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            cam.release()

    cv2.destroyAllWindows()
    img = cv2.imread(img_name,0)
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                          cv2.THRESH_BINARY, 199, 5)
    thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 199, 5) 
    canny = cv2.Canny(img,100,200)
    cv2.imshow('ORIGINAL',img)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sholx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('threshold',th1)
    cv2.imshow('adaptive threshold mean',thresh1)
    cv2.imshow('adaptive threshold gaussian',thresh2)
    cv2.imshow('Canny',canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   

def resolution():
    cam = cv2.VideoCapture(0)
    global res
    cv2.namedWindow("Camera")
    while True:
        img_counter = 0
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Camera", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            cam.release()
    cv2.destroyAllWindows()
    img = cv2.imread(img_name,0)
    lower1 = cv2.pyrDown(img)
    lower1 = cv2.resize(lower1,(800,600))
    lower2 = cv2.pyrDown(lower1)
    lower2 = cv2.resize(lower2,(800,600))
    lower3 = cv2.pyrDown(lower2)
    lower3 = cv2.resize(lower3,(800,600))
    lower4 = cv2.pyrDown(lower3)
    lower4 = cv2.resize(lower4,(800,600))
    lower5 = cv2.pyrDown(lower4)
    lower5 = cv2.resize(lower5,(800,600))
    cv2.namedWindow('Resolution')
    cv2.createTrackbar('Resol','Resolution',0,4,nothing)
    while(1):
        res = cv2.getTrackbarPos('Resol','Resolution')
        if res == 0:
            cv2.imshow('Resolution',lower1)
        elif res == 1:
            cv2.imshow('Resolution',lower2)
        elif res ==2:
            cv2.imshow('Resolution',lower3)
        elif res == 3:
            cv2.imshow('Resolution',lower4)
        elif res == 4:
            cv2.imshow('Resolution',lower5)
        cv2.waitKey(0)
      
    
    
res = 0
def nothing(x):
    pass
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
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
    elif k == ord('s'):
        S = not A
        scan_and_filter()
    elif k == ord('r'):
        resolution()
    elif k == 27:
        break;

    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    res = cv2.getTrackbarPos('Resol','Resolution')
    res = res+1
    resname = 'lower' + str(res)

    color = (b,g,r)
    
    

cv2.destroyAllWindows()
