import numpy as np

print("-----llenar matriz de ceros------")
matriz=np.zeros([6,7]) # 3 filas x 5 columnas 
print(matriz)

print("-----llenar matriz de unos------")
matriz=np.ones ([6,7])
print( matriz )

print("-----llenar matriz de vacios------")
matriz=np.empty([6,7])
print(matriz)

print("-----llenar arreglo con rango------")
# el primer parametro es el valor inicial 
# el segundo parametro es el valor final 
#el tercer parametro es el incremento 
lista=np.arange(0,10,2) 
print(lista)

print("-----llenar arreglo con rango No 2------")
lista=np.arange(0,10,2) 
print(lista)