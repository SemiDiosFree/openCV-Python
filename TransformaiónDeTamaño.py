#aplicar translacion, rotacion, transformacion a fin, etc.
import numpy as np 
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('lobo.jpg',0)
#indicar el factor de escala 
res = cv2.resize(img,None, fx=2, fy=2, interpolation= cv2.INTER_CUBIC)
#indicanco manualmente el nuevo tamaño de la imagen.
height, width = img.shape[:2]
res=cv2.resize(img,(2*width, 2*height),interpolation = cv2.INTER_CUBIC)
#cv2.namedWindow('imagen',cv2.WINDOW_NORMAL)
cv2.imshow('imagen',res)
cv2.waitKey(0)