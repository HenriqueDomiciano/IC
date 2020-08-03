import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
import re 
import sys
np.set_printoptions(threshold=sys.maxsize)

def criar_matriz(rows,columns): 
    
    matriz_valores=np.zeros((rows,columns))
    index=0
    new_value=[]
    with open (r'C:\Users\Dell\Documents\aprender vhdl\sobel_x_opertator\new.txt',"r") as fr:
        value=fr.readlines()
        for lines in value:
            lines=re.sub("\n","",lines)
            new_value.append(lines)
        for i in range (rows):
            for j in range(columns): 
                matriz_valores[i][j]=int(new_value[index])
                index=index+1

    return matriz_valores

new_image=criar_matriz(225,225)
print(new_image) 
plt.imshow(new_image,cmap='gray',vmin=0,vmax=255)
plt.show()
