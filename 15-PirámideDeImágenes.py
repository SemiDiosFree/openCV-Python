#(la piramide de imágenes le da un tratamiento a la imagen 
# como por ejemplo, reduccion de ruido, análisis de textura, 
# reconocimiento d eobjetos, etc)

#Existen dos tipos de parámides de imágenes 
#   1) PIRÁMIDE GAUSSIANA
#   2) PIRÁMIDE LAPLACIANAS

import cv2

img = cv2.imread('lobo.jpg')
baja_res = cv2.pyrDown(img)

mayor_res = cv2.pyrUp(baja_res)

#cv2.namedWindow('baja resolucion',cv2.WINDOW_NORMAL)
cv2.imshow('baja resolucion',baja_res)
cv2.imshow('alta resolucion',mayor_res)
cv2.waitKey(0)