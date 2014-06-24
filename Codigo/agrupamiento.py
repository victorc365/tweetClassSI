import numpy as np
import Pycluster


def cargaDatos(nombreArchivo):
    ## carga la matriz de caracteristicas a clasificar
    return np.load(nombreArchivo)


M=cargaDatos("DataSet.npy")
## proceso de clustering
labels,error,nfound=Pycluster.kcluster(M,5)

print labels
