import cv2
import numpy as np

quant=[]

frame=cv2.imread(r'C:\Users\Dell\Desktop\python\IC\imagens\img_carro_frame_1k.jpg')
cascade_src=r'C:\Users\Dell\Downloads\classifier\cascade.xml'
car_cascade=cv2.CascadeClassifier(cascade_src)
grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
cars=car_cascade.detectMultiScale(grey,2,1)
for (x,y,w,h) in cars: 
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
    quant.append(x)
cv2.imshow('',frame)
cv2.imwrite('harrcascade.png',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
