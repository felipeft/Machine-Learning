#não há um tipo padrão no Python para trabalhar com o conceito de matrizes
#Elas são amplamente utilizadas em Machine Learning. Por exemplo, as Redes Neurais são uma técnica conhecida da área e são basicamente compostas de blocos de matrizes
#como declarar uma variável do tipo array:
import numpy as np
matriz1d = np.array([1, 2, 3])
matriz2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#   [1, 2, 3] 
#   [4, 5, 6]
#   [7, 8, 9]   matriz 3x3

#realizando op matemáticas com esses arrays:
print(matriz1d * 2)
print(matriz1d + matriz1d)

#vendo o tamanho de um array:
print(matriz2d.shape)

#o operador '+' em listas no python concatena duas listas:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

#em array do tipo numpy o operador '+' realiza uma soma elemento a elemento:
print(np.array([1, 2, 3]) + np.array([4, 5, 6]))

#de modo semelhante, o operador '*' em listas faz multiplica-la pelo numero de vezes:
print([1, 2, 3]*3)

#já em array do tipo numpy de fato multiplica todos os elementos:
print(np.array([1, 2, 3]) * 3)

#em resumo, Os operadores + e * funcionam da forma como esperávamos ao lidar com matrizes. Este comportamento permite realizar operações geométricas, como soma de vetores ou pontos, e estatísticas, como cálculo da média.

#matriz de 3 dimensoes = m * n * c
matriz3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
print(matriz1d.ndim)
print(matriz2d.ndim)
print(matriz3d.ndim,'\n')

#multiplicação entre duas matrizes:
#seja A uma matriz M x N e B uma matriz N x P a multiplicaçao entre elas será uma matriz C de M x P
#as dimensoes devem ser compativeis:
matriz2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2d2 = np.array([[20, 12, 10], [16, 55, 45], [33, 27, 18]])
print(matriz2d,'\n')
print(matriz2d2,'\n')
print(np.dot(matriz2d, matriz2d2),'\n')
#a ordem importa
print(np.dot(matriz2d2, matriz2d),'\n')
#realizando a multiplicação com matrizes diferentes
matriz23 = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz23,'\n')
print('dimensoes da primeira matriz: ',matriz23.shape)
print('dimensoes da segunda matriz: ',matriz2d.shape)
print('Só é possbivel realizar a multiplicação 23 x 2d(vai resultar numa matriz 2 x 3) =')
print(np.dot(matriz23, matriz2d))