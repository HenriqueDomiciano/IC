import cv2

cap=cv2.VideoCapture(r'C:\Users\Dell\Downloads\videos\video1.avi')
for n in range(0,50,5):
    if n%5==0:
        _,frame=cap.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        for values in frame:
            for m in values:
                with open('rom.mif','a') as f :
                    m=str(bin(m))[2:]
                    while len(m)<9:
                        m='0'+m
                    f.write(m+'\n')
        print('done ',n) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()