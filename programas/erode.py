import matplotlib.pyplot as plt
import numpy as np
import cv2
n=16
cap=cv2.VideoCapture(0)
while(1 ):
      ret,frame=cap.read()
      kernel=np.ones((n,n),np.uint8)
      imagem2=cv2.erode(frame,kernel)
      cv2.imshow("imagem2",imagem2)
      k = cv2.waitKey(5) & 0xFF
      if k == 27 or n>256: 
         break
cap.release()
cv2.destroyAllWindows()
