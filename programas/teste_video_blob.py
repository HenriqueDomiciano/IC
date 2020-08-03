import cv2 
import numpy as np 
import skimage.feature as skf
import skimage.filters as skfi 
cap = cv2.VideoCapture(0) 
subtractor=cv2.BackgroundSubtractorMOG2()
x,y=[],[]

while(1): 
  
    _, frame = cap.read() 
       
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    mask=subtractor.apply(frame)
    
    #val=skf.blob_doh(mask)

    for i in range (len(val)):
        cv2.circle(frame,(int(val[i][1]),int(val[i][0])), 10, (0,0,255),-1 )
    
    cv2.imshow('grey',mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




cap.release()   
cv2.destroyAllWindows() 
