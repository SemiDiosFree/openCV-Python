 import numpy as np 
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('lobo.jpg',0)
rows,cols,ch = img.shape
pts1 = np.float31([[100,400],[400,100],[100,100]])
pts2 = np.float32([[50,300],[400,200],[80,150]])

M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('input')
plt.subplot(122),plt.imshow(dst),plt.title('output')
plt.show()

cv2.namedWindow('imagen',cv2.WINDOW_NORMAL)
cv2.imshow('imagen',dst)
cv2.waitKey(0)