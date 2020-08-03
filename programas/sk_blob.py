import skimage.feature as skf
import skimage.filters as skfi 
import matplotlib.pyplot as plt 
import numpy as np  
import math
import cv2

n=8
x=[]
y=[]

kernel=np.ones((n,n),np.uint8)

im = cv2.imread(r"C:\Users\Dell\Downloads\imagens\carros.jpg", cv2.IMREAD_GRAYSCALE)

ima= cv2.erode(im,kernel)

tresh_val=skfi.threshold_li(ima,initial_guess=200)

ret,ima= cv2.threshold(ima,tresh_val,255,cv2.THRESH_BINARY)

val=skf.blob_doh(ima,threshold=0.03)



'''for i in range (len(val)):
    try:
        if val[i][2]<15:
            val=np.delete(val,i,0)
    except:
        pass
'''
for i in range(len(val)):
        x.append(val[i][0])
        y.append(val[i][1])



print(len(val))
plt.scatter(y,x,c='g')
plt.imshow(im,cmap='gray')
plt.show()




