import numpy as np 
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('lobo.jpg',0)
rows,cols = img.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),80,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.namedWindow('imagen',cv2.WINDOW_NORMAL)
cv2.imshow('imagen',dst)
cv2.waitKey(0)