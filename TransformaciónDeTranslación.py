import numpy as np 
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('lobo.jpg',0)
rows, cols = img.shape
M = np.float32([ [1,0,210],[0,2,210] ])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.namedWindow('imagen',cv2.WINDOW_NORMAL)
cv2.imshow('imagen',dst)
cv2.waitKey(0)