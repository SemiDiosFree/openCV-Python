#FILTROS PASA ALTO (FPA)

#(muestra todos los operadores en un solo
# diagrama. todos los kernels son de tamaño 
# 3x3)

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('lobo.jpg')

laplacian = cv2.Laplacian(img, cv2.CV_8U)
sobelx = cv2.Sobel(img, cv2.CV_8U,1,0,ksize =3)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)

plt.subplot(2,2,1),plt.imshow(img,cmap ='gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap='gray')
plt.title('Laplaciano'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'),plt.xticks([]),plt.yticks([])

plt.show()