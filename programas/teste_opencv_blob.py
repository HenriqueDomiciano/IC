#!/usr/bin/python

# Standard imports

import cv2
import numpy as np
import skimage.filters as skf
import skimage.morphology as skm 
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf)
n=3
# Read image
im = cv2.imread(r"C:\Users\Dell\Downloads\imagens\carros.jpg", cv2.IMREAD_GRAYSCALE)
ret,im= cv2.threshold(im,140,255,cv2.THRESH_BINARY_INV)
mask=cv2.medianBlur(im, n)
# Setup SimpleBlobDetector parameters.
#radius=10
#selem=skm.disk(radius) 

#local_otsu = skf.rank.otsu(im, selem) 
params = cv2.SimpleBlobDetector_Params()

#plt.imshow(im >= local_otsu, cmap=plt.cm.gray)
#plt.show()
# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)
print(len(keypoints))
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
plt.imshow(im_with_keypoints,cmap='gray')
plt.show()