#metodo utilizado para realizar previsões:
#Método de Monte Carlo (MMC) qualquer método que se baseia em amostragens aleatórias massivas para obter resultados numéricos
#O nome Monte Carlo surgiu durante o projeto Manhattan, na Segunda Guerra Mundial. Por ser secreto, o trabalho exigia um codinome e sugeriram usar o nome Monte Carlo. Referindo-se ao Cassino Monte Carlo, em Mônaco.
#muito empregado para prever dados financeiros da bolsa de valores

#basicamente, em vez de obtermos um dado de forma analitica, vamos realizar inumeras tentativas aleatórias até chegar em um valor

#vamos calular a probabilidade de jogar dois dados e os dois cairem com o mesmo valor utilizando o MMC

import random

num_tentativas = 2000000    #serão feitos 2 milhoes de lancamento de dados
quantidade_acertos = 0

for _ in range (num_tentativas):    #2 milhoes
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)

    if(dado_1 == dado_2):
        quantidade_acertos += 1

print('A probabilidade usando o MMC é: ',quantidade_acertos / num_tentativas) 

#calculando de forma analitica:
#temos 6 possibilidades de os dados estarem identicos
#temos tambem 36 combinações possiveis entre os pares
#logo, a probabilidade de de termos dados iguais é de 6/36 = 0,166666667

#perceba que com mmc o valor foi bem aproximado do esperado
