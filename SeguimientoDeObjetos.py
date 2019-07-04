import cv2
import numpy as np

img = cv2.imread('lobo.jpg')

while(1):
    #toma cada frame
    #_, frame = cap.read

    #conversion BGR a HSV
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #definir el rango de azules en HSV
    alto_Gris = np.array([72,17,64])
    bajo_gris = np.array([38,15,56])
    bajo_verde = np.array([25,50,50])
    alto_verde = np.array([67,255,255])

    #limite de la imagen HSV para obtener solamente colores azules
    mask = cv2.inRange(hsv, alto_Gris, bajo_gris)

    #Mascara bitwise-AND e imagen original
    lobo=cv2.bitwise_and(img, img, mask = mask)
    cv2.imshow('mask',mask)
    cv2.imshow('lobo', lobo)

    k=cv2.waitKey(5) & 0xFF
    #si pulsa 'q' se rompe el ciclo
    if k == ord("q"):
        break
cv2.destroyAllWindows()