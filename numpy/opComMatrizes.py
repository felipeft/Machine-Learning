import numpy as np
ponto_original = np.array([3, 4])
print('Ponto original: ', ponto_original)
rotacao = np.array([[-1.0, 0.0], [0.0, -1.0]])
ponto_rotacionado = np.dot(rotacao, ponto_original)
print('Ponto rotacionado: ', ponto_rotacionado)
translacao = np.array([5.0, 0.0])
ponto_transladado = ponto_original + translacao
print('Ponto transladado: ', ponto_transladado)
escala = 2
ponto_escalonado = ponto_original * escala
print('Ponto escalonado: ', ponto_escalonado, '\n')
#Matrizes são muito aplicadas para realizar operações, como as descritas anteriormente, em jogos, animações e na área da Computação Gráfica. No entanto, essas mesmas operações são também aplicadas em Machine Learning. Todo o processo de aprendizado que um algoritmo de Machine Learning faz envolve um número grande de operações matriciais

#exemplos de inicialização de matrizes:
print(np.zeros((1, 3))) #esse parametro passado é apenas o shape da matriz
print(np.ones((2, 2))) #aqui a matriz é preenchida por 1 com o shape 2 x 2
print(np.full((1, 2), 3))  #é passado o shape e tambem um valor a ser preenchido
print(np.full((2, 1), np.nan))  #o mesmo da linha acima, so que com uma variavel not a number
print(np.arange(5)) #5 funciona como um valor limitante (igual a funçao range)
print(np.arange(0, 2, 0.4)) #temos aqui valor inicial, limitante e tamanho dos passos
print(np.linspace(0, 2, 5)) #Devido a aspectos de imprecisão numérica ao utilizar o float, a função arange nem sempre produz um número consistente de elementos. Nesse caso, é preferível utilizar a função linspace

#é possivel especificar qual tipo de valor é passado na matriz atraves do parametro dtype

#A indexação nos Arrays do Numpy funciona de forma similar à indexação das listas. Na indexação de um array, é possível passar um índice específico, um intervalo sem passo ou um intervalo com passo.

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)
print(matriz[1, 1])
print(matriz[:, 1])
print(matriz[0, :])
print(matriz[:2, 1:],'\n') #duas primeira linhas e duas ultimas colunas

#obtendo arrays de diferentes shapes apartir de uma matriz:
matriz_coluna = np.array([[1, 2], [3, 4], [5, 6]])
print(matriz_coluna.shape)
vetor = matriz_coluna.ravel()
print(vetor)
matriz_linha = matriz_coluna.reshape((2, 3))
print(matriz_linha)
matriz_invalida = matriz_coluna.reshape((2, 4))