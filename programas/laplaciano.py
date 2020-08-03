import cv2 
import numpy as np 
  
#Capture livestream video content from camera 0 
cap = cv2.VideoCapture(0) 
  
while(1): 
  
    # Take each frame 
    _, frame = cap.read() 
      
    # Convert to HSV for simpler calculations 
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    # Calcution of Sobelx 
    sobelx = cv2.Sobel(grey,cv2.CV_8U,1,0,ksize=3) 
      
    # Calculation of Sobely 
    sobely = cv2.Sobel(grey,cv2.CV_8U,0,1,ksize=3) 
      
    # Calculation of some of sbelx+sobely 
    final_image=sobelx+sobely  
    laplacian=cv2.Laplacian(grey,ksize=3,ddepth=cv2.CV_8U)  
    #cv2.imshow('sobelx',sobelx) 
    #cv2.imshow('sobely',sobely) 
    #cv2.imshow('sum',final_image) 
    cv2.imshow("laplacian0",laplacian)
    cv2.imshow('grey',sobelx)
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
  
cv2.destroyAllWindows() 
  
#release the frame 
cap.release() 