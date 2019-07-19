import cv2
import numpy as np 

manzana = cv2.imread('manzana.jpg')
globo = cv2.imread('naranja1.jpg')

#Generar una pirámide Gaussiana para manzana
G = manzana.copy()
gpManz = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpManz.append(G)

#Generar una piramide Gaussiana para globo
G = globo.copy()
gpGlobo = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpGlobo.append(G)

#Generar una piramide laplaciana para manzana
lpManzana = [gpManz[5]]
for i in range (5,0,-1):
    GE = cv2.pyrUp(gpManz[i])
    height, width = gpManz [i-1].shape[:2]
    GE1=cv2.resize(GE,(width, height))
    L = cv2.subtract(gpManz[i-1],GE1)
    lpManzana.append(L)

#Genera una pirámide laplaciana para globo
lpGlobo = [gpGlobo[5]]
for i in range (5,0,-1):
    GE = cv2.pyrUp(gpGlobo[i])
    height, width = gpGlobo[i-1].shape[:2]
    GE1 = cv2.resize(GE,(width,height))
    L= cv2.subtract(gpGlobo[i-1],GE1)
    lpGlobo.append(L)

#Adicciona la mitad izquiera de la imagen 'manzana' con la mitad derecha de la imagen 'globo'
#para cada nivel

LS = []
for la, lb in zip(lpManzana,lpManzana):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:round(cols/2)],lb[:,round(cols/2):]))
    LS.append(ls)

#Reconstruye la imagen final

ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    height, width = LS[i].shape[:2]
    ls_ = cv2.resize(ls_,(width,height))
    ls_ = cv2.add(ls_, LS[i])

#imagen final mezclando directamene las dos imagenes iniciales
# (sin utilizar pirámides)

real = np.hstack((manzana[:,:round(cols/2)],globo[:,round(cols/2):]))

#muestra la imagen de la 'globanza'
cv2.imshow('imagen',ls_)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Guerda ambas imagenes de 'globanza' la obtenida
#utilizando mezcla directa y la obtenida

#utilizando pirámides
cv2.imwrite('mezcla_piramides.jpg',ls_)
cv2.imwrite('mezcla_directa.jpg',real)