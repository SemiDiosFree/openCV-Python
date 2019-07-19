import cv2 
import numpy as np 

img= cv2.imread('lobo.jpg',0)


kernel = np.ones((7,7),np.uint8)

########    EROSIÓN  #######
erosion = cv2.erode(img,kernel,iterations=1)

########    DILATACIÓN  #######
dilatacion = cv2.dilate(img,kernel, iterations=1)

########    APERTURA  #######
#es util para eliminar el ruido
apertura = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

########    CIERRE  #######
cierre = cv2.morphologyEx(img, cv2.MORPH_CLOSE,kernel)

########    GRADIENTE MORFOLOGICO  #######
gradiente = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


cv2.namedWindow('kernel',cv2.WINDOW_NORMAL)
cv2.imshow('kernel',kernel)
cv2.namedWindow('erosion',cv2.WINDOW_NORMAL)
cv2.imshow('erosion',erosion)
cv2.namedWindow('dilatacion',cv2.WINDOW_NORMAL)
cv2.imshow('dilatacion',dilatacion)
cv2.namedWindow('apertura',cv2.WINDOW_NORMAL)
cv2.imshow('apertura',apertura)
cv2.namedWindow('cierre',cv2.WINDOW_NORMAL)
cv2.imshow('cierre',cierre)
cv2.namedWindow('gradiente',cv2.WINDOW_NORMAL)
cv2.imshow('gradiente',gradiente)
cv2.waitKey(0)
cv2.destroyAllWindows()