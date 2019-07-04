import numpy as np 
import cv2

#crear una imagen en negro
img=np.zeros((512,512,3), np.uint8)

#Dubuja una linea horizontal verde con grosor de 4px
img=cv2.line(img, (5,100), (505,100),(0,255,0),6)

#Dibuja un cuadrado
img = cv2.rectangle(img,(210,360),(300,500),(255,0,0),8)

#dibuja un circulo
img = cv2.circle(img,(255,255), 100, (0,0,255), 4)

#dibuja una elipse
img = cv2.ellipse(img,(255,105),(100,50),0,0,180,255,5)

#dibujar un triangulo de color amarillo
pts = np.array([[180,120],[330,120],[255,140]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

#Agregar texto a las imagenes
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'DRAWING',(40,90), font, 3,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('imagen',img)
cv2.waitKey(0)

