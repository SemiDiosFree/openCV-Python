import numpy as np 
import cv2

img=cv2.imread('lobo.jpg')
px=img[100,100]
print(px)

#accesando solamente al pixel azul
blue = img[100,100,0]
print (blue)

img[100,100]= [255,255,255]
print (img[100,100])

#accediendo al valor rojo
img.item(10,10,2)
#modificando el valor rojo
img.itemset((10,10,2),100)
img.item(10,10,2)
#accediendo a las propiedades de la imagen
#contiene numero de filas, columnas y canales
print(img.shape)

#acceder al numero total de pixeles 
print(img.size)

#Tipo de datos de la imagen
print(img.dtype)

#DIVIDIENDO Y COMBINANDO CANALES DE IMAGEN
#los canales R,G,B de una imagen pueden dividirse en sus planos individuales
#luego pueden combinarse nuevamente dichos canales para nuevamente
#formar una imagen
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

b=img[:,:,0]
img[:,:,2]=0

cv2.imshow('1',img)
cv2.waitKey(0)
