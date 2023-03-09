#analisar as vendas dos ultimos 10 anos por mes
import numpy as np
#cada linha é um ano (10 anos) e cada coluna representa um mês
vendas_anos = np.array([[149, 499, 112, 430, 115, 390, 187, 316, 361, 483, 353, 400], 
[258, 222, 461, 263, 384, 210, 452, 372, 417, 364, 468, 397],
[259, 329, 417, 132, 318, 256, 362, 496, 232, 132, 306, 174], 
[117, 148, 480, 201, 160, 292, 146, 209, 298, 215, 358, 234], 
[169, 229, 381, 119, 225, 270, 379, 272, 167, 332, 144, 359], 
[358, 434, 228, 300, 122, 247, 142, 127, 191, 356, 450, 308], 
[105, 251, 317, 147, 214, 280, 289, 338, 498, 133, 304, 225], 
[156, 165, 299, 461, 290, 123, 451, 450, 353, 191, 167, 451], 
[149, 377, 389, 176, 103, 439, 269, 132, 200, 391, 426, 175], 
[137, 107, 229, 227, 198, 206, 432, 169, 323, 141, 155, 233]])
print(vendas_anos.shape)

#calculo da media de uma matriz:
print(np.mean(vendas_anos))

#calculando a media do primeiro ano apenas:
primeiro_ano = vendas_anos[0, :]
print('No primeiro ano temos uma média de: ', primeiro_ano.mean())
#o shape de primeiro_ano será (12,). sempre bom verificar isso para ter certeza

#O parâmetro axis representa o eixo no qual você quer fazer a operação. Como assim? Um eixo da matriz é o mesmo que a dimensão. Ah! Lembre-se que a matriz vendas_anos é uma matriz de tamanho 10x12, contendo 10 linhas e 12 colunas. Por ter linhas e colunas, tem dimensão 2, ou seja, tem 2 eixos. O primeiro eixo, ou eixo 0, é o das linhas. O segundo eixo é o das colunas. 

print(primeiro_ano.mean(axis=0))   #a variavel primeiro_ano é um vetor unidimensional, so tem o eixo 0

#Quando o parâmetro axis é especificado com o valor 0, a função mean vai calcular a média dos elementos de todo aquele eixo
#Agora, calcule para o eixo igual a 1. A função mean vai calcular a média ao longo de todas as colunas

#logo, para calcularmos a media de todos os anos com um simples comando basta:
media_ano = vendas_anos.mean(axis=1)
print(media_ano)
print(media_ano.shape,'\n')

#para calcularmos a media dos meses ao longo de todos os anos basta fazer o contrario:
media_meses = vendas_anos.mean(axis=0)
print(media_meses)
print(media_meses.shape,'\n')

#encontrando o maior numero de vendas ao longo dos anos:
soma_ano = vendas_anos.sum(axis=1)  
print(soma_ano.shape)
print(soma_ano)
maximo_vendas_anuais = soma_ano.max()   
print(maximo_vendas_anuais,'\n')

#é possivel passar o parametro axis na funçao max. entao ela vai pegar o maior valor daquele eixo
print(vendas_anos.max(axis=0))
print(vendas_anos.max(axis=1),'\n')

#agora queremos encontrar a posicao do maior valor:
indice_max = soma_ano.argmax()
print(indice_max)
print(soma_ano[indice_max])

#supondo que os 10 últimos anos sejam o intervalo de 2011 a 2021, calcule o mês de maior venda em cada ano e imprima essas informações:

import locale
from datetime import datetime
anos = np.arange(2011, 2021)    #basicamente um array de anos
meses = list(map(lambda x: datetime.strptime(str(x), "%m"), np.arange(1, 13)))  #vai mapeando todos os 12 meses na lista meses
meses = list(map(lambda x: x.strftime("%B").title(), meses))    #vai dando o nome dos meses a lista meses
print(anos)
print(meses,'\n')
for i in range(len(anos)):
    indice_max_ano = vendas_anos[i, :].argmax()
    maior_venda_ano = vendas_anos[i, indice_max_ano]
    print(f"A maior venda de {anos[i]} ocorreu no mês de {meses[indice_max_ano]} e foi de {maior_venda_ano}.")

