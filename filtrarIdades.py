#imagine que voce tenha que fazer um programa que separe em idades, grupos de pessoas que irao se vacinar
#Podemos tomar como base essa funçao filtrar:

# def filtrar(lista, limiar):
#     nova_lista = []
#     for elemento in lista: 
#         if elemento > limiar:
#             nova_lista.append(elemento)
#     return nova_lista

#em vez de lotarmos a funçao de if's e else's, vamos criar uma funçao para cada fase
def primeira_fase(idade):
    return idade >= 75

def segunda_fase(idade):
    return  60 <= idade <= 74

def terceira_fase(idade):
    return idade <= 59

#basta modificar a funçao filtrar para receber essas outras funçoes
def filtrar(lista, criterio):
    nova_lista = []
    for elemento in lista:
        if criterio(elemento):
            nova_lista.append(elemento)
    return nova_lista
#criterio é um parametro qualquer, porem na linha 25 ele é tratado como uma funçao e se comportará de acordo com a funçao passada como argumento
#normalmente os codigos de programação funcional nao utilizam laços de repetiçao e sim recursão

idades = [30, 45, 60, 72, 75, 99]
primeiro_grupo = filtrar(idades, primeira_fase)
segundo_grupo = filtrar(idades, segunda_fase)
terceiro_grupo = filtrar(idades, terceira_fase)

# print(primeiro_grupo)
# print(segundo_grupo)  
# print(terceiro_grupo)

# O código é bastante intuitivo, de fácil legibilidade e facilmente escalável. Ele é escalável, porque, caso surjam novas fases, por exemplo, quarta_fase, será necessário criar somente uma nova função e passar para filtrar como argumento