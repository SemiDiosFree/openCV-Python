import sklearn
from sklearn import datasets
import pandas as pd 

#lee el dataset y pasa los datos a una DataFrame
#de pandas por comodidad.
iris1 = datasets.load_iris()
sk_iris = datasets.load_iris()
#el dataset contiene 4 atributos
print(iris1.feature_names)
#separar iris setosa de las otras especies en función de la longitud
#del pétalo(tercer atributo)
for value in iris1.data[:, 2]:
    if value > 2:
        print('Iris setosa')
    else:
        print('Iris virginica o Iris versicolor')


iris = pd.DataFrame(data=sk_iris.data, columns=sk_iris.feature_names)
iris['label'] = pd.Categorical.from_codes(sk_iris.target, sk_iris.target_names)
#Se descarta la familia setosa que ya se tiene clasificada
iris = iris[iris.label != 'setosa']
virginica = iris.label == 'virginica'
#obtener un array con los nombres de las caracteristicas que se midieron
feature = iris.columns[:4]
#inicializar en valor de precisión
best_acc = 0.0
for fi in feature: 
    thresh = iris[fi].copy()
    thresh.sort_values(inplace=True)

    for t in thresh: 
        pred =(iris[fi] > t)
        acc = (pred ==virginica).mean()
        if acc > best_acc:
            best_acc = acc
            best_fi = fi
            best_t  = t

print('Mejor precisión obtenida: {:.1%}'.format(best_acc))
print('Mejor característica para clasificar: {}'.format(best_fi))
print('Valor óptimo umbral: {} cm'.format(best_t))