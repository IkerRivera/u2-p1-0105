import numpy as np

califas=np.array([60,70,90])
print("------------- ej 1 imrpimir califas -----")
print(califas)#imprime la lista de califas
print(type(califas))#muestra  el tipo de arreglo
print("------------- ej 0 dimensiones de un array  -----")
califas=np.array(60)
print(califas)
print("dimensiom :", califas.ndim)
print("------------- ej 1 de dimensiones de un array  -----")
califas=np.array([60,70,90])
print(califas)
print("dimensiom :", califas.ndim)
print("------------- ej 2 de dimensiones  de un array-----")
califas=np.array([
    [60,70,90],
    [50,89,96]
]) # un arreglo de 2 dimenciones es como una tabla en excel
print(califas)
print("dimensiom :", califas.ndim)
print("------------- ej 3  de dimensiones de un array  -----")
califas=np.array([
    [
    [60,70,90],
    [50,80,98]
    ],
    [
    [60,70,90],
    [50,80,98]
    ]
]) # un arreglo de 2 dimenciones es como una tabla en excel
print(califas)
print("dimensiom :", califas.ndim)