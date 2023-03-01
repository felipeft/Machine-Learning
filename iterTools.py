import itertools

contador = itertools.count()
#contador recebe um iterador que foi retornado da funçao count

print(contador)
print(next(contador))
print(next(contador),'\n')

print(itertools.combinations("ABC", 2)) #retorna um objeto iteravel, e nao uma lista
print(list(itertools.combinations("ABC", 2)))   #converteu o objeto a uma lista, combinações 2 a 2 
print(list(itertools.combinations("AABC", 2)))  #ha repetiçoes devido a "A" ser considerado 2 caracter
print(list(itertools.combinations("ABCD", 3)),'\n')  # a ordem aqui nao importa, e nao ha repeticoes

#permutações
print(list(itertools.permutations([1, 1])))
print(list(itertools.permutations([1, 2])))
#acima temos permutações com dois elementos, a funçao considera r=2 devido ao tamanho da lista
print(list(itertools.permutations([1, 2, 3])))
#r=3 é considerado aqui
print(list(itertools.permutations([1, 2, 3], r=2)),'\n')
#o r=2 foi passado como parametro, criando permutações com 2 elementos

#produto cartesiano
print(list(itertools.product([1, 2], repeat = 2)))  # A x B = (x1,y1) X (x2, y2)
#esse repeat = 2 indica que vamos repetir a lista de entrada [1, 2] 2 vezes, o mesmo que fazer itertools.product([1,2], [1,2])
print(list(itertools.product(['Python'], ['Academy', 'Rocks']))) #produto cartesiano de duas listas de tamanhos diferentes
print(list(itertools.product([1, 2], [3, 4], [5, 6])))  #2 x 2 x 2 = 8

