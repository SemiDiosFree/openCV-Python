#alisando o suavizando imágenes.
#los filtros Pasa bajo (FPB) eliminan el contenido de alta frecuencia
#(ej: ruido y bordes) de la imágen, lo que resulta, en imágenes con bordes más borrosos



import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('lobo.jpg')
blur= cv2.blur(img,(3,3))

plt.subplot(),plt.imshow(img), plt.title('original-')
plt.xticks([]),plt.yticks([])
plt.show()

######  TÉCNICA DE PROMEDIADO   #######
plt.subplot(),plt.imshow(blur),plt.title('Difuminada')
plt.xticks([]), plt.yticks([])
plt.show()

#####   FILTRO GAUSSIANO    #####
blur = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(),plt.imshow(blur),plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.show()

#####   FILTRO DE MEDIANA   ######
mediana = cv2.medianBlur(img,5)
plt.subplot(),plt.imshow(blur),plt.title('Mediana')
plt.xticks([]), plt.yticks([])
plt.show()