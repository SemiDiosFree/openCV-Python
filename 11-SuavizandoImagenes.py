#CONVOLUCIÓN 2D
import cv2
import numpy as np 
from matplotlib import pyplot as plt 
img = cv2.imread('lobo.jpg')

#crea el kernel
kernel = np.ones((5,5),np.float32)/25

#filtra la image utilizando el kernel anterior
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Promediada')
plt.xticks([]),plt.yticks([])
plt.show()