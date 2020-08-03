import cv2
import numpy as np
n=3
a=0
cap=cv2.VideoCapture(r'C:\Users\Dell\Downloads\videos\video.avi')
cascade_src=r'C:\Users\Dell\Downloads\classifier\cascade.xml'
car_cascade=cv2.CascadeClassifier(cascade_src)
kernel=np.ones((n,n))
#kernel=np.ones((13,13),np.uint8)
while (1):
    ret,frame=cap.read()
    if type(frame)==type(None):
        break
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(grey,4,2)

    for (x,y,w,h) in cars: 
        cv2.rectangle(frame,(x,y),(w+x,h+y),(0,255,0),2)
    cv2.imshow("harr",frame)
    if a == 10:
        cv2.imwrite('imagemrelat1.png',frame)
    a+=1
    key=cv2.waitKey(100)   
    if key==27 :
        break
cap.release()
cv2.destroyAllWindows()

