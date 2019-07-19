import numpy as np 
import cv2
cap=cv2.VideoCapture(0)

while(True):
    #Captura video cuadro a cuadro
    ret, frame=cap.read()
    
    #Las operaciones sobre los cuadros se hacen aquí
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    color = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGRA)
    
    #Muestra el cuadro resultante
    cv2.imshow('frame',gray)
    cv2.imshow('color',color)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
#cuando todo esta listo se libera la captura.
cap.release()
cv2.destroyAllWindows()