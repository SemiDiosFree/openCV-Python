import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('lobo.jpg',0)
bordes = cv2.Canny(img,180,260)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Imágen original'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(bordes,cmap = 'gray')
plt.title('Bordes de la imagen'),plt.xticks([]),plt.yticks([])

plt.show()