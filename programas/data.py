import cv2
import numpy as np
import matplotlib.pyplot as plt
import statistics
import sys 


np.set_printoptions(threshold=sys.maxsize)

def image_data():
    imagem=cv2.imread(r'C:\Users\Dell\Downloads\imagens\pensando.jpg')
    imagem=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY,cv2.CV_8U)
    cols,rows=imagem.shape
    a=np.zeros((2,rows))
    b=np.zeros((cols+4,2))
    imagem=np.concatenate((a,imagem),axis=0)
    imagem=np.concatenate((imagem,a),axis=0)
    imagem=np.concatenate((b,imagem),axis=1)
    imagem=np.concatenate((imagem,b),axis=1)

    return imagem



def filtro_linha(img,start,stop,slope):
    lines= len (img)
    columns=len(img[0])
    for i in range (lines):
        for j in range (columns):
            if (img[i][j] < start) and (img[i][j] > stop): 
                img[i][j]=img[i][j]
            else:
                img[i][j]=int(img[i][j]*(slope))
    return img


def inverse(img):
    lines=len(img)
    columns=len(img[0])
    for i in range (lines):
        for j in range (columns):
            img[i][j]=255-img[i][j]
    return img


def log_filter(img,a):
    lines= len (img)
    columns=len(img[0])
    x=np.linspace(0,255,256)
    y=a*(np.log10(1+x))
    plt.plot(x,y)
    plt.show()
    for i in range (lines):
        for j in range (columns):
            img[i][j]= int(a*np.log10(img[i][j]+1))
            if img[i][j]>256:
                img[i][j]=255
    return img


def filtro_potencia(img,a,c):
    lines= len (img)
    columns=len(img[0])
    x=np.linspace(0,255,256)
    y=(c*(x**a))
    plot=plt.plot(x,y)
    plt.show()
    for i in range (lines):
        for j in range (columns):
            img[i][j]= int(c*(img[i][j]**a))
            if img[i][j]>256:
                img[i][j]=255
    return img
def histogram_normalization(img):
    values=['black']*3004
    bins=np.linspace(0,255,256)
    #plt.hist(img,bins=bins,histtype='step',color=values)
    plt.hist(img,bins=bins,density=True,log=True,histtype='step',color=values)
    plt.show()



def filtro_laplaciano(img):
    lines=len(img)
    rows=len(img[0])
    new_img=np.zeros((lines,rows))

    for i in range (0,lines):
        try:
            for j in range(0,rows):
                if (i != lines-2) and (j !=rows-2):
                    try:
                        new_img[i][j]=(-1*img[i][j]+(-1*img[i][j+1])+(-1*img[i][j+2])+(-1*img[i+1][j])+(8*img[i+1][j+1])+(-1*(img[i+1,j+2]))+((-1*img[i+2][j]))+(-1*img[i+2][j+1])+(-1*img[i+2][j+2]))
                    except IndexError: 
                        break
        except IndexError:
                break
    return(new_img)            
           
def filtro_de_media(img):
    lines=len(img)
    rows=len(img[0])
    new_img=np.zeros((lines,rows))

    for i in range (0,lines):
        try:
            for j in range(0,rows):
                if (i != lines-2) and (j !=rows-2):
                    try:
                        new_img[i][j]=int((1/9)*(img[i][j]+(img[i][j+1])+(img[i][j+2])+(img[i+1][j])+(img[i+1][j+1])+((img[i+1,j+2]))+((img[i+2][j]))+(img[i+2][j+1])+(img[i+2][j+2])))
                        if new_img[i][j]<0:
                            new_img[i][j]=0
                    except IndexError: 
                        break
        except IndexError:
                break
    return(new_img)
    
def filtro_de_mediana(img):
    lines=len(img)
    rows=len(img[0])
    new_img=np.zeros((lines,rows))
    median_vector=np.zeros(9)
    for i in range (0,lines):
        try:
            for j in range(0,rows):
                if (i != lines-2) and (j !=rows-2):
                    try:
                        median_vector=[img[i][j],img[i][j+1],img[i][j+2],img[i+1][j],img[i+1][j+1],img[i+1,j+2],img[i+2][j],img[i+2][j+1],img[i+2][j+2]]                           
                        new_img[i][j]=statistics.median(median_vector)

                        if new_img[i][j]<0:
                            new_img[i][j]=0
                    except IndexError: 
                        break
        except IndexError:
                break
    return(new_img)
    

val=image_data()
#new_image=filtro_potencia(val,1.2,0.3)
#new_image=cv2.Sobel(val,cv2.CV_8U,0,1,ksize=3)
#new_image=inverse(val)
#new_image=log_filter(val,100)
#new_image=filtro_potencia(val,5,0.1)
#histogram_normalization(val)
new_image=filtro_de_media(val)
new_image=filtro_laplaciano(new_image)
#new_image=filtro_de_mediana(val)
cv2.imwrite('imagemfinal4.png',new_image)
#plot=plt.matshow(new_image,cmap='gray',vmin=0,vmax=255
