import numpy as np
import Pycluster


def cargaDatos(nombreArchivo):
    ## carga la matriz de caracteristicas a clasificar
    return np.load(nombreArchivo)


M=cargaDatos("DataSet.npy")
## proceso de clustering
## hacemos varias corridas
c=[]
for i in range(5):
    labels,error,nfound=Pycluster.kcluster(M,5)
    c.append(labels)

z=np.array(c)
np.save("resultados.npy",z)
print labels
