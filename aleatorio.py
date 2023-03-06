import random
print(random.random())
print(random.random())  #retorna o próximo número decimal aleatório no intervalo [0.0, 1.0)

#criando uma funçao que gera valores maiores que 1 entre um determinado intervalo
def minha_funcao_random(num_min, num_max):
    diferença = num_max - num_min
    return diferença * random.random() + num_min

print(minha_funcao_random(10, 20))

#definindo um valor de semente
random.seed(10)
print(random.random())
print(random.random())

random.seed(1234)
print(random.random())
print(random.random())

#existe uma funçao em random que faz o mesmo que minha_funcao_random, no caso uniform

print(random.uniform(10, 20))