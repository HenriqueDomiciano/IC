#funciona somente com video1 por enquanto
import numpy as np 
import cv2
import time
n=0
contador=[]
first_road,second_road,third_road,four_road=[],[],[],[] 
distancia=0
kernel=np.ones((25,25))
kernel2=np.ones((3,3))
x0,y0=30,90
x1,y1=70,90
x2,y2=130,90
x3,y3=180,90

def localization(img,kern,posx,posy):
    soma=0 
    for i in range (posx,posx+len(kern)):
        for j in range (posy,posy+len(kern[0])):
            soma=soma+img[i,j]
    
    return soma/((len(kern)**2)*255)

def pre_process(img): 
    #kernel=np.ones((n,n))
    imagem=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imagem=cv2.equalizeHist(imagem)
    imagem=cv2.GaussianBlur(imagem,(7,7),0)
    return imagem

n,frame=0,0
cap=cv2.VideoCapture(r'C:\Users\Dell\Downloads\videos\video1.avi')
subtractor = cv2.createBackgroundSubtractorMOG2(history=400, detectShadows=False,)
while True:
    _,frame=cap.read()
    
    if n%5==0 and n>10:
        try:
            frame=pre_process(frame)
            frame=subtractor.apply(frame)
            frame=cv2.dilate(frame,kernel2)
            frame_with_squares=cv2.rectangle(frame,(x0,y0),(x0+25,y0+25),(255,0,0),2)
            frame_with_squares=cv2.rectangle(frame_with_squares,(x1,y1),(x1+25,y1+25),(255,0,0),2)
            frame_with_squares=cv2.rectangle(frame_with_squares,(x2,y2),(x2+25,y2+25),(255,0,0),2)
            frame_with_squares=cv2.rectangle(frame_with_squares,(x3,y3),(x3+25,y3+25),(255,0,0),2)
        except: 
            break
        cv2.imshow('1',frame_with_squares)
        val0=localization(frame,kernel,x0,y0)
        val1=localization(frame,kernel,x1,y1)
        val2=localization(frame,kernel,x2,y2)
        val3=localization(frame,kernel,x3,y3)
        if val0>0.5:
            first_road.append(val0)
        if val1>0.5:
            #print(val1)
            second_road.append(val1)
        if val2>0.5:

            third_road.append(val2)
        if val3>0.5:
            four_road.append(val3)
    print('na 1a pista são',len(first_road))
    print('na segunda pista são', len(second_road))
    print('na teceira pista sao',len(third_road))
    print('na quarta pista sao',len(four_road))
    print(n)
    n=n+1
    key = cv2.waitKey(30)
    print(n)
    if key == 27 :
        break
cv2.imwrite('image_fundo.jpg',frame)
'''
print('na 1a pista são',len(first_road))
print('na segunda pista são', len(second_road))
print('na teceira pista sao',len(third_road))
print('na quarta pista sao',len(four_road))
'''
cap.release()
cv2.destroyAllWindows()
    