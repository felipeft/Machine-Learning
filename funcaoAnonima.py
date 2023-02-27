def quadratica(x):
    return x*x

#pode ser reescrito apenas como:
lambda x: x*x

#podemos utilizar mais de um argumento
lambda a,b: a+b

lambda x: x[0].upper() + x[1:]

#para chamar essas funçoes, basta atribui-las a variaveis:
f = lambda x: x[0].upper() + x[1:]
s = lambda a,b: a+b
print(f('olá mundo!'))

#vamos reduzir as funçoes de filtrarIdades:
import filtrarIdades
primeiro_grupo = filtrarIdades.filtrar(filtrarIdades.idades, lambda x: x >= 75)
segundo_grupo = filtrarIdades.filtrar(filtrarIdades.idades, lambda x: 60 <= x <= 74)
terceiro_grupo = filtrarIdades.filtrar(filtrarIdades.idades, lambda x: x <= 59)

print(primeiro_grupo)
print(segundo_grupo)  
print(terceiro_grupo)