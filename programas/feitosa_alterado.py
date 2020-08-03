import cv2
import numpy as np

def contador_de_pixels(img,value_y,value_x,size_of_kernel):
    val=np.array([])
    for i in range(size_of_kernel):
        for j in range(size_of_kernel):
            val1[i,j]=img[i+value_y,j+value_x]
    return val1.sum()

blob=0
x,y=42,104
x1,y1=104,104
x2,y2=145,104
x3,y4=199,104
cap=cv2.VideoCapture(r'C:\Users\Dell\Downloads\videos\video1.avi')
subtractor=cv2.BackgroundSubtractorMOG2(history=30,detect_shadows=False)

while True :
    val1,val2,val3,val4=0,0,0,0
    _,frame=cap.read()
    frame=subtractor.apply(frame)
    valu1=contador_de_pixels(frame,y,x,2)
    valu2=contador_de_pixels(frame,y1,x1,2)
    valu3=contador_de_pixels(frame,y2,x2,2)
    valu4=contador_de_pixels(frame,x3,y3,2)

    if valu1>89000 or valu2>89000  or valu3>89000 or valu4>89000: 
        blob=blob+1
    print(blob)

    key = cv2.waitKey(30)
    if key == 27 :
        break
cap.release()
cv2.destroyAllWindows()
         
