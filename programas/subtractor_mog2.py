import cv2
import numpy as np
import skimage.feature as skf

cap = cv2.VideoCapture(r'C:\Users\Dell\Downloads\videos\highway.mp4')

#out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))

subtractor = cv2.createBackgroundSubtractorMOG2(history=300, detectShadows=True,)

params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 100

a=0
n=23
#kernel=np.ones((n,n),np.uint8)

while True:
    a=a+1
    _, frame = cap.read()
    mask = subtractor.apply(frame)
    mask=cv2.medianBlur(mask, n)
    mask=255-mask
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(mask)
    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints= cv2.line(im_with_keypoints,(0,500),(1280,500),(0,0,255),2)
    im_with_keypoints=cv2.line(im_with_keypoints,(0,300),(1280,300),(0,0,255),2)

        #out = cv2.VideoWriter('output.mp4', -1, 20.0, (640,480))

    cv2.imshow("resukt",mask)
    cv2.imshow('result2',im_with_keypoints)

    key = cv2.waitKey(30)
    if key == 27 or a==151:
        break
cv2.imwrite("secondsaved.jpg",im_with_keypoints)
cv2.imwrite('thirdsave.jpg',mask)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()