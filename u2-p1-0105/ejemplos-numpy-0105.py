import numpy as np

califas=np.array([60,70,90])
print("------------- ej 1 imrpimir califas -----")
print(califas)#imprime la lista de califas
print(type(califas))#muestra  el tipo de arreglo
print("------------- ej 0 dimensiones de un array  -----")
califas=np.array(60)
print(califas)
print("dimensiom :", califas.ndim)
print("------------- ej 1 de dimensiones  -----")
califas=np.array([60,70,90])
print(califas)
print("dimensiom :", califas.ndim)
print("------------- ej 2 de dimensiones  -----")
califas=np.array([
    [60,70,90]
    [50,89,96]
])
print(califas)
print("dimensiom :", califas.ndim)