import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier

#leemos el dataset y pasamos los datos a una Dataframe de pandas por comdidad
sk_iris = datasets.load_iris()
iris = pd.DataFrame(data=sk_iris.data, columns=sk_iris.feature_names)
#que las etiquetas sean de tipo categorical será importante más adelante 
#a la hora de crear los gráficos
iris['labels']= pd.Categorical.from_codes(sk_iris.target, sk_iris.target_names)
X = iris[['petal length (cm)', 'petal width (cm)']] #tomar el ancho y la longitud del petalo
y = iris['labels'].astype('category')

n_neighbors = 15
h = .02          # step size de la malla
# Creamos los colormap
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    # Creamos una instancia de Neighbors Classifier y hacemos un fit a partir de los
    # datos.
    # Los pesos (weights) determinarán en qué proporción participa cada punto en la
    # asignación del espacio. De manera uniforme o proporcional a la distancia.
    clf = KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y.cat.codes)
    # Creamos una gráfica con las zonas asignadas a cada categoría según el modelo
    # k-nearest neighborgs. Para ello empleamos el meshgrid de Numpy.
    # A cada punto del grid o malla le asignamos una categoría según el modelo knn.
    # La función c_() de Numpy, concatena columnas.
    x_min, x_max = X.iloc[:, 0].min() - 1, X.iloc[:, 0].max() + 1
    y_min, y_max = X.iloc[:, 1].min() - 1, X.iloc[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    # Ponemos el resultado en un gráfico.
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    # Representamos también los datos de entrenamiento.
    plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y.cat.codes, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))
    plt.xlabel('Petal Width')
    plt.ylabel('Petal Length')
    plt.savefig('iris-knn-{}'.format(weights))
    plt.show()