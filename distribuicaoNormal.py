#normalvariate (μ, σ)
# μ é a média e σ é o desvio padrão 

import random
print(random.normalvariate(0, 1))

#gerando um inteiro aleatório:
print(random.randint(1, 6)) #simulação de jogar um dado

#tirando um valor aleatorio de uma lista(exemplo):
#usaremos a funçao choice para isso
dado = [1, 2, 3, 4, 5, 6]
print(random.choice(dado))

#vamos simular um dado viciado:
pesos = [1,1,1,1,2,4]
print(random.choices(dado, weights = pesos))    #maior o peso, maior a chance de ser 
#40% de chance de sair 6 e 20% de sair 5

#alem disso, é possivel atribuir quantos valores podem ser gerados  
print(random.choices(dado, weights = pesos, k = 10),'\n')

#tratando de jogos, vamos utilizar a funçao shuffle que embaralha uma lista de elementos(muito utilizadas em jogos)

baralho = ['Ás de Copas','2 de Copas','3 de Copas','4 de Copas','5 de Copas','6 de Copas','7 de Copas','8 de Copas','9 de Copas','10 de Copas','Valete de Copas','Dama de Copas','Rei de Copas']

random.shuffle(baralho) #embaralhou a lista acima

print(baralho, '\n')

#choices faz reposiçao, o elemento escolhido pode ser retornado mais de uma vez

#Ao invés de embaralhar os elementos, podemos pegar uma amostra aleatória dos dados, utilizando o método Sample (que significa amostra), que retorna uma lista de comprimento k de elementos exclusivos escolhidos a partir da sequência ou conjunto da população. O método Sample é usado para amostragem aleatória sem reposição, ou seja, ao retornar um elemento aleatório de uma lista, aquele elemento não poderá mais ser retornado novamente, isso faz com que cada elemento aleatório só seja retornado uma única vez.

print(random.sample(baralho, k = 2),'\n')    #retiramos uma amostra de k = 2 elementos sem reposiçao 