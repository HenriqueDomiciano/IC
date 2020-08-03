import cv2 
import numpy as np  
import matplotlib.pyplot as plt 
import skimage.feature as skf
import skimage.filters as skfi 
from transform import read_and_write
a,n=0,0
cap=cv2.VideoCapture(r"C:\Users\Dell\Downloads\videos\video1.avi")

while(n<26): 
    _,frame= cap.read() 
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    a=a+5
    if a%5==0: 
        read_and_write(frame,n)
        n=n+1
        print(n) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




cap.release()   
cv2.destroyAllWindows() 