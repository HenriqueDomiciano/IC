import cv2 
import numpy as np 
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

def read_and_write(u):
    #print(img)
    '''
    with open ("rom"+str(u)+".mif",'w') as f :
        for i in range (0,len(img)):
            for j in range (0,len(img[0]) ):
                    f.write(str(int(img[i][j])))
                    f.write('\n')
    '''
    with open('values_of_rom.txt','w') as fr: 
        for r in range(1,u+1):
            fr.write("rom"+str(r)+".mif")
            fr.write('\n')
    
def newfunction(path): 
    with open (path,'r') as fr :
        fil= fr.readlines()
    with open (path,'w') as fw:
        for files in fil: 
            while len(files) < 10 :
                files = '0' + files  
            fw.write(files)
read_and_write(25)
#newfunction("rom.mif")