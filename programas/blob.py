import cv2 
import numpy as np 
import matplotlib.pyplot as plt

blobi=0

np.set_printoptions(threshold=np.inf)

class Bloob:
    def __init__(self,x,y,h,w):
        self.x=x
        self.y=y
        self.h=h
        self.w=w

img=cv2.imread(r'C:\Users\Dell\Pictures\teste.png')
img_g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

for i in range(len(img_g)):
    for j in range(len(img_g[0])):
        if img_g[i][j]<100:
            img_g[i][j]=0
        else: 
            img_g[i][j]=1

inicial=True
blob=[]
dist=[]
b=0
c=0
def distancia(x,y,x0,y0):
    return((((x-x0)**2)**0.5)+(((y-y0)**2)**0.5))

for i in range(len(img_g)):
    for j in range(len(img_g[0])):
        if img_g[i][j]==1 and (inicial):
            blob.append(Bloob(j,i,1,1))
            inicial=False
        elif img_g[i][j]==1:
            #for r in range(len(blob)):
                #print(r,'...',blob[r].x,blob[r].y)
            while (c < len(blob)) :
                dist.append(distancia(blob[c].x,blob[c].y,j,i))
                c=c+1
            if (min(dist)>80):
                    blob.append(Bloob(j,i,0,0))
                    dist=[]
                    c=0
            elif (min(dist)<80):
                #ind=dist.index(min(dist))
                #print(ind)
                blob[c-1].x, blob[c-1].y = j,i
                dist=[]
                c=0
        else:
            pass      

for r in range(len(blob)):
    print(blob[r].x,blob[r].y)
'''plt.imshow(img_g,cmap="gray")
plt.show()
'''