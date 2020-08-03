import cv2 
import numpy as np
from matplotlib import pyplot as plt 
imagem=cv2.imread(r"C:\Users\Dell\imagem_equalized.jpg",1)
imagem=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
pix=cv2.calcHist([imagem],[0],None,[256],[0,256])
for i in range (len(imagem)):
    for j in range(len(imagem[0])): 
        if imagem[i][j]<20: 
            imagem[i][j]=0
        else :
            imagem[i][j]=1
plt.xlabel('intensidade de pixel')
plt.ylabel('número de pixel')
bins=np.linspace(0,255,256)
#plt.imshow(imagem,cmap='binary')
plt.plot(pix)
plt.show()
